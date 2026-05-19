# 🌿 Projeto: Integração IoT e Monitoramento Agrícola (Oracle)

Este projeto realiza a transposição da lógica de controle IoT (desenvolvida na Fase II) para um ambiente de dados robusto no Oracle, permitindo análises temporais e espaciais de culturas agrícolas.

## 📋 Visão Geral
* **Base IoT:** O código original estabeleceu as regras de negócio para monitoramento de NPK, pH e umidade.
* **Simulação:** O script gerOU 4 anos de dados históricos (2022-2025) para 100 fazendas, simulando sazonalidade e consumo de nutrientes.
* **Dados:** Datasets consolidados prontos para carga no Banco Oracle.

## ⚙️ Pré-requisitos

### Ambiente Python
Para gerar novos datasets ou modificar a simulação, é necessário ter instalado:
* **Bibliotecas:** `pandas`, `numpy`
    * Instalação via terminal: `pip install pandas numpy`

### Ambiente Oracle
* **Oracle SQL Developer** configurado.
* **Configuração de Importação (Crítico):**
    * **Delimitador:** `;` (Ponto e vírgula).
    * **Separador Decimal:** `,` (Vírgula).
    * **Formato de Data:** `YYYY-MM-DD`.

## 🚀 Como utilizar
1. **Geração:** Execute `python Sensores_Dataset.py` para criar ou atualizar os arquivos CSV.
2. **Carga:** Importe os arquivos CSV no Oracle respeitando as configurações regionais indicadas acima.
3. **Validação:** Utilize os comandos disponíveis no arquivo com os modelos de select para verificar a consistência dos dados (Ex: contagem por fazenda, sazonalidade da bomba, status de nutrientes).

## Equipe 👥
Heitor Exposito de Sousa - RM 566013
Marco Antônio Rodrigues Siqueira - RM 569975
Nádia Nakamura Vieira - RM 568906
Rafael Bassani - RM 569930
Vinicius Xavier da Silva - RM 572108

### Ativos do repositório

Repositório GitHub: https://github.com/AI-FIAP-2026/farmtech-solutions/tree/main/src/fase_3/cap_1

**1. código fonte e lógica de negócio**

* `irrigacao.ino`: código original de hardware (fase 2) que serviu de base para a lógica de sensores.
* `Sensores_Dataset.py`: script python responsável pela simulação e geração do dataset robusto para os dados agrícolas.

**2. bases de dados (datasets)**

* `sensores_v8_final.csv`: volume principal de dados históricos de leituras (umidade, ph, npk, status da bomba).
* `clientes_v7.csv`: dados cadastrais das empresas/clientes proprietários das fazendas.
* `fazendas_v8_final.csv`: informações geográficas e detalhamento das propriedades rurais.
* `cultivo_v7.csv`: metadados das simulações de cultivo, áreas e status de qualidade.

**3. documentação e consultas técnicas**

* `Fase3_Cap1_BancoOracle_v2.docx`: documentação oficial dos passos e metodologia do projeto.
* `Select_Banco.txt`: registro das consultas sql utilizadas para validação, verificação de sazonalidade e lógica de reposição de nutrientes.

## Vídeo Demonstrativo 📺
Assista à demonstração da solução e das interfaces: https://youtu.be/0ck84D-usvI
