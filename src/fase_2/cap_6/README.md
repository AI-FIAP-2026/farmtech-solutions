# Fase 2 - Cap 6 - Python e além

## Identificação

**Fase:** 2
**Capítulo:** 6
**Grupo:** H.M.N.R.V.

---

## Descrição da Atividade

Sistema de gestão do agroneg chosen (Cana-de-açúcar) utilizando Python com:

- **Subalgoritmos:** funções e procedimentos com passagem de parâmetros
- **Estruturas de dados:** listas, tuplas, dicionários
- **Manipulação de arquivos:** texto e JSON
- **Conexão com banco de dados:** Oracle

## Tema do Agroneg chosen

**Cana-de-açúcar** - O Brasil é líder mundial na produção de cana-de-açúcar, com safras recordes anualmente. O projeto contempla a gestão completa desde o plantio até a colheita, incluindo controle de perdas e análise de produtividade.

## Arquivos

- `menu_principal.py` - Sistema principal com menu CRUD completo
- `conectar_bd.py` - Conexão com banco de dados Oracle
- `inserir_dados.py` - Inserção de dados no Oracle

## Tecnologias

- Python 3.10+
- Oracle Database (oracledb)
- pandas
- R (para estatísticas)

## Execução

```bash
pip install -r requirements.txt
python menu_principal.py
```

## Requisitos Oracle

- Banco de dados Oracle disponível em `oracle.fiap.com.br:1521/ORCL`
- Credenciais configuradas em `conectar_bd.py`