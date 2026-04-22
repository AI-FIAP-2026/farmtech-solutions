# Definir biblioteca pessoal para instalação de pacotes
if (!dir.exists(Sys.getenv("R_LIBS_USER"))) {
  dir.create(Sys.getenv("R_LIBS_USER"), recursive = TRUE)
}
.libPaths(c(Sys.getenv("R_LIBS_USER"), .libPaths()))

# Carregar pacotes necessários
if (!require("dplyr")) install.packages("dplyr")
library(dplyr)

if (!require("ggplot2")) install.packages("ggplot2")
library(ggplot2)

# Leitura dos dados
args <- commandArgs(trailingOnly = FALSE)
script_path <- grep("^--file=", args, value = TRUE)
if (length(script_path) == 0) {
  script_dir <- getwd()
} else {
  script_dir <- dirname(sub("^--file=", "", script_path))
}
dados <- read.csv(file.path(script_dir, "dados_plantio.csv"), stringsAsFactors = FALSE)

# Visualizar os dados
print("Dados de plantio:")
print(dados)

# Estatísticas gerais básicas
media_area <- mean(dados$area, na.rm = TRUE)
desvio_area <- sd(dados$area, na.rm = TRUE)
media_qnt_insumo <- mean(dados$qnt_insumo, na.rm = TRUE)
desvio_qnt_insumo <- sd(dados$qnt_insumo, na.rm = TRUE)

# Agrupamento para limpeza de dados (removendo redundâncias do log de insumos)
dados_limpos <- dados %>%
  group_by(cultura, area) %>%
  summarise(
    lucro_total = max(lucro, na.rm = TRUE),
    peso_total = max(peso, na.rm = TRUE),
    metodo = first(na.omit(metodo)),
    .groups = "drop"
  ) %>%
  filter(!is.na(lucro_total) & !is.na(area))

cat("\n== Estatísticas Gerais ==\n")
cat("Média da área plantada:", round(media_area, 2), "m²\n")
cat("Desvio padrão da área plantada:", round(if(is.na(desvio_area)) 0 else desvio_area, 2), "m²\n")
cat("Média da quantidade de insumos:", round(media_qnt_insumo, 2), "\n")

# --- LÓGICA DE REGRESSÃO COM SEGURANÇA ---
cat("\n== Análise de Regressão ==\n")

plot(dados_limpos$area, dados_limpos$lucro_total,
     main = "REGRESSÃO: ÁREA X LUCRO (METODOS DE COLHEITA)",
     xlab = "Área (m²)", ylab = "Lucro (R$)",
     pch = 16, col = "#9d9d9d")

# Função auxiliar para aplicar regressão apenas se houver dados suficientes (n > 1)
aplicar_regressao <- function(df_sub, cor_linha) {
  if (nrow(df_sub) > 1) {
    modelo <- lm(lucro_total ~ area, data = df_sub)
    abline(modelo, col = cor_linha, lwd = 2)
    return(TRUE)
  }
  return(FALSE)
}

# Separação por métodos
dados_drone <- subset(dados_limpos, metodo == "Drone Agrícola")
dados_trator <- subset(dados_limpos, metodo == "Pulverizador Tratorizado")

sucesso_drone <- aplicar_regressao(dados_drone, "darkorange2")
sucesso_trator <- aplicar_regressao(dados_trator, "slategray")

if(sucesso_drone) cat("- Modelo para Drone gerado com sucesso.\n")
if(sucesso_trator) cat("- Modelo para Trator gerado com sucesso.\n")
if(!sucesso_drone && !sucesso_trator) cat("- Dados insuficientes para linhas de tendência.\n")

legend("topleft", legend=c("Drone", "Trator"), col=c("darkorange2", "slategray"), lty=1, lwd=2)

# Correlação
if (nrow(dados_limpos) > 1) {
  correl <- cor(dados_limpos$area, dados_limpos$lucro_total, use = "complete.obs")
  cat("Correlação Geral (Área x Lucro):", round(correl, 4), "\n")
}

# Estatísticas por cultura
estatisticas_por_cultura <- dados %>%
  group_by(cultura) %>%
  summarise(
    media_area = mean(area, na.rm = TRUE),
    media_qnt_insumo = mean(qnt_insumo, na.rm = TRUE),
    .groups = "drop"
  )

cat("\n== Estatísticas por Cultura ==\n")
print(estatisticas_por_cultura)