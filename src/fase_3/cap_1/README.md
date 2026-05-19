# Entrega Obrigatória — Fase 3, Capítulo 1

## Objetivo
Organizar e disponibilizar um conjunto de dados e scripts para demonstração de uso do Oracle Database (Oracle SQL Developer) com dados de sensores agrícolas, incluindo consultas exemplo e evidências da importação.

## Uso dos dados da Fase 2
Os datasets desta entrega complementam e reutilizam informações geradas na Fase 2. Considere a consistência de chaves (IDs de fazenda, cultivo e sensor) ao relacionar tabelas entre fases.

## Importação dos CSVs no Oracle SQL Developer
Passos resumidos:
- Abra o Oracle SQL Developer.
- Crie um esquema ou conecte-se ao esquema destino.
- Use a opção de importação de dados (`Tools` → `Import` ou clicando com o botão direito na tabela destino) para carregar cada CSV em tabelas temporárias ou definitivas.
- Ajuste tipos de dados (NUMBER, DATE, VARCHAR2) conforme necessário e defina separador como `,`.

Arquivos CSV disponíveis em `datasets/`:
- clientes_v7.csv
- cultivo_v7.csv
- fazendas_v8_final.csv
- sensores_v8_final.csv

## Consultas SQL realizadas
As consultas usadas como exemplo estão em `sql/consultas_oracle.sql`. Incluem instruções de criação simples de tabelas, loads e consultas de verificação (SELECT com JOINs entre fazendas, cultivo e sensores).

## Evidências
A pasta `evidencias/` contém prints e arquivos demonstrando a importação e execução das consultas. Se ainda não houver arquivos, deixe como espaço para upload de imagens.

## Estrutura das pastas
```
src/fase_3/cap_1/
├── datasets/         # CSVs usados na importação
├── scripts/          # scripts Python e Arduino (Sensores_Dataset.py, irrigacao.ino)
├── sql/              # consultas e scripts SQL (consultas_oracle.sql)
├── evidencias/       # prints e evidências (vazio por padrão)
└── README.md         # este documento
```

## Instruções de execução dos scripts
- `scripts/Sensores_Dataset.py`: script Python de exemplo para pré-processamento dos arquivos antes da importação. Execute com o Python 3 em ambiente que tenha as dependências listadas em `requirements.txt` do repositório (se aplicável):

```
python3 src/fase_3/cap_1/scripts/Sensores_Dataset.py
```

- `scripts/irrigacao.ino`: sketch Arduino para controle de irrigação. Abra no Arduino IDE ou PlatformIO e envie para a placa compatível.

## Link do vídeo demonstrativo
Adicione aqui o link do vídeo demonstrativo (YouTube / Drive / outro).

## Observações
- Não altere os arquivos das fases anteriores sem necessidade.
- Este README resume os passos; detalhes das consultas e cargas estão em `sql/consultas_oracle.sql`.
