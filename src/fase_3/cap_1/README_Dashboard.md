# 🌿 Projeto: Dashboard de Gestão Agrícola

Este projeto é um dashboard interativo desenvolvido em **Python** utilizando a biblioteca **Streamlit** para visualização de dados. O sistema consome dados em tempo real (ou históricos) de um banco de dados **Oracle** para monitorar indicadores cruciais de fazendas, como status de irrigação, reposição de nutrientes e níveis de umidade do solo.

## 🚀 Como Executar o Projeto

Para rodar este dashboard em sua máquina, siga os passos abaixo:

### 1. Pré-requisitos

Certifique-se de ter o Python instalado. Você precisará instalar as bibliotecas necessárias. Abra o seu terminal e execute:

```bash
pip install streamlit pandas oracledb plotly

```

### 2. Configuração do Banco de Dados

O código está configurado para conectar-se ao banco de dados da FIAP. Verifique se as variáveis no início do script (`USER`, `PASSWORD`, `DSN`) estão corretas conforme o seu ambiente:

```python
USER = "seu_usuario"
PASSWORD = "sua_senha"
DSN = "host:porta/servico"

```

### 3. Execução

No terminal, navegue até a pasta onde salvou o arquivo (ex: `app.py`) e execute o comando:

```bash
streamlit run app.py

```

O navegador abrirá automaticamente com o dashboard rodando em `http://localhost:8501`.

---

## 📊 Detalhamento dos Gráficos

O dashboard utiliza a biblioteca **Plotly** para fornecer visualizações dinâmicas e interativas:

### 1. Total de Irrigação (Mensal)

* **Tipo:** Gráfico de Barras (`px.bar`).
* **O que mostra:** A frequência de acionamento do sistema de irrigação ("Bomba Ligada") ao longo dos meses.
* **Utilidade:** Ajuda a identificar picos de consumo de água e períodos de seca em cada fazenda.

### 2. Ocorrências de Reposição de Nutrientes (N, P, K)

* **Tipo:** Gráfico de Barras Empilhadas (`barmode='stack'`).
* **O que mostra:** O volume de reposições dos macronutrientes (Nitrogênio, Fósforo e Potássio) acumuladas por mês.
* **Utilidade:** Permite visualizar o esforço de fertilização e identificar se a reposição de nutrientes segue um padrão sazonal ou conforme o desgaste do solo.

### 3. Projeção de Umidade para 2026

* **Tipo:** Gráfico de Linhas (`px.line`) com marcadores.
* **O que mostra:** A tendência de umidade do solo com base no histórico anterior, agrupado por Estado e Cultura.
* **Linhas de Referência:**
* **Linha Verde (Tracejada):** Nível mínimo aceitável para cultura de Café (45%).
* **Linha Laranja (Pontilhada):** Nível mínimo aceitável para cultura de Soja (55%).
* **Utilidade:** Ferramenta preditiva que auxilia no planejamento preventivo, indicando quando o solo estará abaixo dos limites críticos de umidade para diferentes culturas.

---

## 🛠 Funcionalidades Extras

* **Filtros em Cascata:** A barra lateral permite filtrar por `Estado` -> `Cultura` -> `Cliente` -> `Fazenda`. Os filtros são inteligentes: ao selecionar um estado, as opções subsequentes são atualizadas para refletir apenas os dados relacionados àquela seleção.
* **Tratamento de Dados:** O código inclui limpeza de dados (conversão de vírgula para ponto em strings, formatação de datas e cálculo de "delta" para identificar mudanças de status de nutrientes).

---

## Equipe 👥
Heitor Exposito de Sousa - RM 566013
Marco Antônio Rodrigues Siqueira - RM 569975
Nádia Nakamura Vieira - RM 568906
Rafael Bassani - RM 569930
Vinicius Xavier da Silva - RM 572108

---

### Ativos do repositório

Repositório GitHub: https://github.com/AI-FIAP-2026/farmtech-solutions/tree/main/src/fase_3/cap_1

**1. Código fonte**

* `Dashboard.py`: script python responsável por criar o dashboard.

**2. Bases de dados Oracle, orinunda dos datasets abaixo**

* `sensores_v8_final.csv`: volume principal de dados históricos de leituras (umidade, ph, npk, status da bomba).
* `clientes_v7.csv`: dados cadastrais das empresas/clientes proprietários das fazendas.
* `fazendas_v8_final.csv`: informações geográficas e detalhamento das propriedades rurais.
* `cultivo_v7.csv`: metadados das simulações de cultivo, áreas e status de qualidade.

---

## Vídeo Demonstrativo 📺
Assista à demonstração da solução e das interfaces: https://youtu.be/Xqunrf7JC_4
