# Definir biblioteca pessoal para instalação de pacotes
if (!dir.exists(Sys.getenv("R_LIBS_USER"))) {
  dir.create(Sys.getenv("R_LIBS_USER"), recursive = TRUE)
}
.libPaths(c(Sys.getenv("R_LIBS_USER"), .libPaths()))

# Carregar pacotes necessários (se ainda não estiverem instalados)
if (!require("dplyr")) install.packages("dplyr")
library(dplyr)

# Leitura dos dados
# O CSV deve ter colunas: cultura, area, tipo_insumo, qnt_insumo
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

#1. Cálculo para a área plantada

media_area <- mean(dados$area, na.rm = TRUE)
desvio_area <- sd(dados$area, na.rm = TRUE)

#2. Calculo para o lucro com base no meio de colheita
mecanica_apenas <- subset(dados, colheita == "MECÂNICA")
manual_apenas <- subset(dados, colheita == "MANUAL")

dp_peso_mecanica <- sd(mecanica_apenas$perda_peso, na.rm = TRUE)
dp_lucro_mecanica <- sd(mecanica_apenas$lucro, na.rm = TRUE)


summary(manual_apenas$lucro)
summary(manual_apenas$peso_perdido)
dp_lucro_manual <- sd(manual_apenas$lucro, na.rm = TRUE)
dp_peso_manual <- sd(manual_apenas$perda_peso, na.rm = TRUE)

#3. Calculo para correlação

cores <- ifelse(dados$colheita == "MECÂNICA", "slategray", "darkorange2")
reg_lin_al <- lm(lucro ~ area, data = dados) #Regressão Linear áreaxlucro
reg_lin_ap <- lm(peso_perdido ~ area, data = dados) #Regressão Linear áreaxpeso

par(mfrow = c(1,2))
plot(dados$area, dados$lucro,
  col = cores,
  pch = 16,
  main = "Dispersão: Área x Colheita",
  xlab = "m²",
  ylab = "R$")
abline(reg_lin_al, col = "#ff00ff", lwd = 2)
legend("topleft",
       legend = c("Mecânica", "Manual"),
       col = c("slategray", "darkorange2"),
       pch = 16,
       bty = "n")

plot(dados$area, dados$peso_perdido,
  col = cores,
  main = "Dispersão Área x Peso perdido",
  pch = 16,
  xlab = "m²",
  ylab = "kg")
abline(reg_lin_ap, col = "#ff00ff", lwd = 2 )
legend("topleft", 
  legend = c("Mecânica", "Manual"),
  col = c("slategray", "darkorange2"),
  pch = 16,
  bty = "n")

correl_mecanica <- cor(mecanica_apenas$area, mecanica_apenas$lucro)
correl_manual <- cor(manual_apenas$area, manual_apenas$lucro)


print("== Estatísticas Gerais Colheita MECÂNICA ==\n")
print("LUCRO: ")
summary(mecanica_apenas$lucro)
print("PESO PERDIDO: ")
summary(mecanica_apenas$peso_perdido)
cat("Desvio Padrão lucro: ", dp_lucro_mecanica)
cat("Desvio Padrão peso perdido: ", dp_peso_mecanica)
cat("Dispersão Área x Lucro: ", correl_mecanica)

cat("== Estatísticas Gerais Colheita Manual ==\n")
print("LUCRO: ")
summary(manual_apenas$lucro)
print("PESO PERDIDO: ")
summary(manual_apenas$peso_perdido)
cat("Desvio Padrão lucro: ", dp_lucro_manual)
cat("Desvio Padrão peso perdido: ", dp_peso_manual)
cat("Dispersão Área x Lucro: ", correl_manual)



