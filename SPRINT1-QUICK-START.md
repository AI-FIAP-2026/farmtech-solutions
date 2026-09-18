# Guia Rápido: Sprint 1 Sompo

## 🎯 Objetivo da Sprint
Estruturar a base do projeto Challenge Sompo com análise de negócio, proposta de solução e arquitetura técnica.

## 📊 Backlog em Um Olhar

```
ISSUES ABERTAS: 11
├─ 1 Epic Pai (#46)
└─ 10 Subtarefas (#47-#57)

DISTRIBUIÇÃO:
├─ 🔴 ALTA:   7 issues (64%)
├─ 🟡 MÉDIA:  4 issues (36%)
└─ 🔵 TAMANHO: 5-8pts (8x), 8-13pts (3x)
```

## 🔢 Todas as Issues

| # | Título | Tipo | Prioridade | Tamanho |
|---|--------|------|-----------|---------|
| **46** | Enterprise Challenge - Sprint 1 - Sompo | Epic | 🔴 | Epic |
| **47** | Análise do Problema e Personas | Task | 🔴 | M |
| **48** | Fatores de Risco Ambientais/Operacionais | Task | 🔴 | M |
| **49** | Estruturação de Dataset e Variáveis | Feature | 🔴 | L |
| **50** | Análise Exploratória dos Dados | Task | 🟡 | M |
| **51** | Definição do Modelo Preditivo | Task | 🔴 | M |
| **52** | Design da Arquitetura Técnica | Task | 🔴 | M |
| **53** | Detalhamento das Integrações | Task | 🟡 | M |
| **54** | Planejamento de Próximas Sprints | Task | 🟡 | L |
| **55** | Estruturação do README.md | Task | 🔴 | L |
| **56** | Gravação de Vídeo de Apresentação | Task | 🔴 | M |
| **57** | Validação Final e Revisão | Task | 🔴 | M |

## 📈 Timeline (Caminhos Críticos)

**Caminho 1: Análise → Dados → EDA**
```
#47 (2d) → #48 (1d) → #49 (2d) → #50 (1d) = 6 dias
```

**Caminho 2: Análise → Modelo → Arquitetura**
```
#47 (2d) → #48 (1d) → #51 (1d) → #52 (1d) → #53 (1d) = 6 dias
```

**Caminho 3: Planejamento (Paralelo)**
```
#54 (2d) = 2 dias [pode ser paralelo]
```

**Convergência: Documentação & Entrega**
```
#55 (2d) → #56 (1d) → #57 (1d) = 4 dias
```

**Total Estimado: 8-10 dias** (em paralelo)

## 📁 Arquivos a Criar/Atualizar

### Novos Arquivos (#47-#57)
```
docs/
├── analise-negocio.md           ← #47
├── fatores-risco.md              ← #48
├── modelo-preditivo.md           ← #51
├── arquitetura.md                ← #52
├── integracao-servicos.md        ← #53
├── analise-exploratoria.md       ← #50
├── roadmap.md                    ← #54
└── sprint-backlog.md             ← #54

data/
├── schema.md                     ← #49
├── dicionario_dados.md           ← #49
└── exemplo_dataset.csv           ← #49

scripts/
└── eda.py                        ← #50

assets/
├── arquitetura-sistema.drawio    ← #52
└── analise/
    ├── heatmap-correlacao.png
    ├── distribuicoes.png
    └── ...outros gráficos
```

### Arquivos Atualizados
```
README.md                    ← #55 (integra tudo)
```

## 🚀 Como Iniciar

### 1️⃣ Hoje: Leitura & Planejamento
- [ ] Ler [docs/SPRINT1-BACKLOG.md](docs/SPRINT1-BACKLOG.md)
- [ ] Ler [SPRINT1-RESUMO.md](SPRINT1-RESUMO.md)
- [ ] Revisar issues #47-#57 no GitHub

### 2️⃣ Dia 1-2: Começar #47 (Análise)
```bash
# Criar arquivo base
mkdir -p docs
touch docs/analise-negocio.md

# Estrutura mínima:
# - Contexto do problema
# - Por que é relevante
# - 3+ personas identificadas
# - Matriz de requisitos por persona
```

### 3️⃣ Dia 2-3: Começar #48 (Fatores)
```bash
# Criar arquivo base
touch docs/fatores-risco.md

# Estrutura mínima:
# - Fatores ambientais listados
# - Fatores operacionais listados
# - Fatores externos listados
# - Tipos de dados por fator
# - Matriz de impacto
```

### 4️⃣ Dia 3-4: Começar #49 (Dataset)
```bash
# Criar estrutura de dados
mkdir -p data
touch data/schema.md
touch data/dicionario_dados.md

# Gerar dados simulados
python scripts/generate_dataset.py > data/exemplo_dataset.csv
# (você vai criar este script como parte de #49)
```

### 5️⃣ Dia 4+: Paralelo com #50-54
- EDA em Python/R
- Proposta de modelo ML
- Diagrama de arquitetura
- Planejamento de Sprints

### 6️⃣ Dia 6+: Convergência
- Integrar tudo no README (#55)
- Gravar vídeo (#56)
- Validar tudo (#57)

## 🔗 Links Rápidos

### GitHub
- **Issues Sprint 1**: https://github.com/AI-FIAP-2026/farmtech-solutions/issues?q=is%3Aopen
- **Project Board**: https://github.com/orgs/AI-FIAP-2026/projects/1
- **Repo**: https://github.com/AI-FIAP-2026/farmtech-solutions

### Documentação
- **Backlog Completo**: [docs/SPRINT1-BACKLOG.md](docs/SPRINT1-BACKLOG.md)
- **Resumo Executivo**: [SPRINT1-RESUMO.md](SPRINT1-RESUMO.md)
- **Brief Original**: [Enterprise Challenge - Sprint 1 - Sompo.md](Enterprise%20Challenge%20-%20Sprint%201%20-%20Sompo.md)

## ✅ Checklist de Sucesso

- [ ] Todas as 11 issues foram criadas (#46-#57)
- [ ] Issues têm descrições detalhadas com checklists
- [ ] Dependências estão mapeadas e documentadas
- [ ] Timeline estimada é realista (8-10 dias)
- [ ] Estrutura de entrega está clara
- [ ] Equipe compreendeu o backlog
- [ ] GitHub Project está configurado
- [ ] Commit inicial foi feito

## 📞 Suporte

**Dúvidas sobre uma issue?**
1. Abra a issue no GitHub (#XX)
2. Leia a descrição completa com checklist
3. Consulte [docs/SPRINT1-BACKLOG.md](docs/SPRINT1-BACKLOG.md) para contexto
4. Verifique dependências (quais issues precisa feito antes)

---

**Última Atualização**: 2026-04-09  
**Status**: ✅ Backlog Pronto para Execução
