# Sprint 1 - Challenge Sompo: Backlog Estruturado

**Gerado em**: 2026-04-09  
**Projeto**: FarmTech Solutions - Grupo H.M.N.R.V.  
**Challenge**: Sompo Seguros - Previsão de Riscos em Equipamentos Agrícolas  
**Link do Projeto**: https://github.com/orgs/AI-FIAP-2026/projects/1

---

## 📋 Visão Geral

Este documento detalha o backlog completo da **Sprint 1** do Challenge Sompo, quebrado em **11 subtarefas granulares** mapeadas diretamente para **11 GitHub Issues** ([#46-#57](https://github.com/AI-FIAP-2026/farmtech-solutions/issues?q=is%3Aopen+is%3Aissue+label%3Asompo)).

### Objetivo da Sprint
Estruturar a base do projeto com foco em:
1. Compreensão do problema de negócio
2. Identificação de personas e requisitos
3. Definição da arquitetura técnica
4. Proposição do modelo preditivo
5. Documentação completa

### Escopo
- ✅ Sem código funcional obrigatório
- ✅ Dados simulados coerentes com cenários reais
- ✅ Documentação como entregável principal
- ✅ Repositório privado no GitHub com estrutura clara

---

## 🎯 Issue Pai

| # | Título | Tipo | Status |
|---|--------|------|--------|
| **46** | **Enterprise Challenge - Sprint 1 - Sompo** | **Epic** | **OPEN** |

**Descrição**: Estruturação da base do projeto Challenge Sompo. Inclui análise de negócio, definição de datos, proposta de modelo de IA e arquitetura técnica.

---

## 📌 Subtarefas (11 Issues)

### Bloco 1: Análise de Negócio (Issues #47-48)

#### #47: [Task] Análise do Problema de Negócio e Personas
- **Prioridade**: 🔴 Alta
- **Tamanho**: 🔵 Medium (5-8 pts)
- **Responsabilidade**: Compreender contexto do problema
- **Dependências**: Nenhuma (início)
- **Checklist**:
  - [ ] Documentar contexto do problema (equipamentos agrícolas, riscos)
  - [ ] Explicar relevância e impactos (custos, falhas, acidentes)
  - [ ] Identificar 3+ personas (operador, gestor, seguradora)
  - [ ] Descrever necessidades por persona
  - [ ] Criar matriz de requisitos
- **Entrega**: `docs/analise-negocio.md`
- **Link**: [GitHub #47](https://github.com/AI-FIAP-2026/farmtech-solutions/issues/47)

#### #48: [Task] Identificação de Fatores de Risco Ambientais e Operacionais
- **Prioridade**: 🔴 Alta
- **Tamanho**: 🔵 Medium (5-8 pts)
- **Responsabilidade**: Mapear variáveis de risco
- **Dependências**: #47 (contexto de negócio)
- **Checklist**:
  - [ ] Listar fatores ambientais (clima, solo, água, topografia)
  - [ ] Listar fatores operacionais (equipamento, velocidade, carga, histórico)
  - [ ] Listar fatores externos (localização, sazonalidade, legislação)
  - [ ] Definir tipo de dados por fator
  - [ ] Criar matriz de impacto/relevância
- **Entrega**: `docs/fatores-risco.md`
- **Link**: [GitHub #48](https://github.com/AI-FIAP-2026/farmtech-solutions/issues/48)

---

### Bloco 2: Estrutura de Dados (Issues #49-50)

#### #49: [Feature] Estruturação de Dataset e Variáveis
- **Prioridade**: 🔴 Alta
- **Tamanho**: 🟢 Large (8-13 pts)
- **Responsabilidade**: Definir schema e criar dados simulados
- **Dependências**: #48 (fatores de risco)
- **Checklist**:
  - [ ] Definir schema de dados (tabelas/estrutura)
  - [ ] Listar variáveis com tipos (numérico, categórico, datetime)
  - [ ] Criar exemplo dataset com 50-100 registros
  - [ ] Documentar dicionário de dados
  - [ ] Validar coerência com cenários reais
- **Entrega**: 
  - `data/schema.md` (definição)
  - `data/exemplo_dataset.csv` (dados)
  - `data/dicionario_dados.md` (documentação)
- **Link**: [GitHub #49](https://github.com/AI-FIAP-2026/farmtech-solutions/issues/49)

#### #50: [Task] Análise Exploratória dos Dados Simulados
- **Prioridade**: 🟡 Média
- **Tamanho**: 🔵 Medium (5-8 pts)
- **Responsabilidade**: Análise inicial de padrões e correlações
- **Dependências**: #49 (dataset criado)
- **Checklist**:
  - [ ] Calcular estatísticas descritivas (média, mediana, desvio padrão)
  - [ ] Identificar distribuições das variáveis
  - [ ] Análise de correlação entre fatores
  - [ ] Gerar visualizações (histogramas, scatter plots, heatmaps)
  - [ ] Documentar insights encontrados
- **Entrega**:
  - `docs/analise-exploratoria.md`
  - `scripts/eda.py` (script de análise)
  - `assets/analise/` (gráficos)
- **Link**: [GitHub #50](https://github.com/AI-FIAP-2026/farmtech-solutions/issues/50)

---

### Bloco 3: Solução de IA/ML (Issues #51-53)

#### #51: [Task] Definição e Justificativa do Modelo Preditivo
- **Prioridade**: 🔴 Alta
- **Tamanho**: 🔵 Medium (5-8 pts)
- **Responsabilidade**: Propor abordagem de ML
- **Dependências**: #48 (fatores de risco), #49 (dados)
- **Checklist**:
  - [ ] Definir tipo de modelagem (classificação, regressão, score, clustering)
  - [ ] Descrever algoritmo proposto (ex: Random Forest, Logistic Regression)
  - [ ] Documentar entrada do modelo
  - [ ] Documentar saída esperada (classe de risco, score)
  - [ ] Justificar abordagem escolhida
  - [ ] Descrever métricas de avaliação (precisão, recall, F1)
- **Entrega**: `docs/modelo-preditivo.md`
- **Link**: [GitHub #51](https://github.com/AI-FIAP-2026/farmtech-solutions/issues/51)

#### #52: [Task] Design da Arquitetura Técnica da Solução
- **Prioridade**: 🔴 Alta
- **Tamanho**: 🔵 Medium (5-8 pts)
- **Responsabilidade**: Desenhar fluxo completo do sistema
- **Dependências**: #51 (modelo definido)
- **Checklist**:
  - [ ] Criar diagrama entrada → processamento → saída
  - [ ] Definir componentes principais (coleta, preprocessamento, modelo, API, UI)
  - [ ] Especificar tecnologias (stack Python/JS/Cloud)
  - [ ] Documentar fluxo de dados
  - [ ] Definir interfaces (APIs, webhooks)
  - [ ] Considerar escalabilidade e performance
- **Entrega**:
  - `docs/arquitetura.md`
  - `assets/arquitetura-sistema.drawio` (ou PNG)
- **Link**: [GitHub #52](https://github.com/AI-FIAP-2026/farmtech-solutions/issues/52)

#### #53: [Task] Detalhamento das Integrações e Serviços
- **Prioridade**: 🟡 Média
- **Tamanho**: 🔵 Medium (5-8 pts)
- **Responsabilidade**: Especificar integrações externas
- **Dependências**: #52 (arquitetura)
- **Checklist**:
  - [ ] Definir APIs de previsão meteorológica
  - [ ] Definir integração com GPS/IoT de equipamentos
  - [ ] Documentar serviços de cloud (AWS/GCP/Azure)
  - [ ] Especificar autenticação e autorização
  - [ ] Definir logging e monitoramento
  - [ ] Documentar SLAs
- **Entrega**: `docs/integracao-servicos.md`
- **Link**: [GitHub #53](https://github.com/AI-FIAP-2026/farmtech-solutions/issues/53)

---

### Bloco 4: Planejamento e Documentação (Issues #54-57)

#### #54: [Task] Planejamento das Próximas Sprints e Roadmap
- **Prioridade**: 🟡 Média
- **Tamanho**: 🟢 Large (8-13 pts)
- **Responsabilidade**: Planejar fases futuras
- **Dependências**: Todas as análises anteriores
- **Checklist**:
  - [ ] Definir escopo Sprint 2 (desenvolvimento parcial)
  - [ ] Definir escopo Sprint 3 (integração e refinamento)
  - [ ] Criar lista de dependências entre sprints
  - [ ] Estimar esforço por etapa
  - [ ] Definir critérios de aceição
  - [ ] Identificar riscos e mitigações
- **Entrega**:
  - `docs/roadmap.md`
  - `docs/sprint-backlog.md`
- **Link**: [GitHub #54](https://github.com/AI-FIAP-2026/farmtech-solutions/issues/54)

#### #55: [Task] Estruturação e Redação do README.md
- **Prioridade**: 🔴 Alta
- **Tamanho**: 🟢 Large (8-13 pts)
- **Responsabilidade**: Documentação centralizada
- **Dependências**: Todas as tarefas anteriores
- **Checklist**:
  - [ ] Estruturar seções principais (problema, solução, personas, dados, modelo, arquitetura)
  - [ ] Integrar links para documentos de suporte
  - [ ] Adicionar diagramas visuais
  - [ ] Adicionar instruções para futuros desenvolvedores
  - [ ] Garantir navegação clara
  - [ ] Revisar formatação e legibilidade
- **Entrega**: Atualizar `README.md` com seções Sprint 1
- **Link**: [GitHub #55](https://github.com/AI-FIAP-2026/farmtech-solutions/issues/55)

#### #56: [Task] Gravação de Vídeo de Apresentação (até 5 min)
- **Prioridade**: 🔴 Alta
- **Tamanho**: 🔵 Medium (5-8 pts)
- **Responsabilidade**: Apresentação visual do desafio
- **Dependências**: #55 (README completo)
- **Checklist**:
  - [ ] Definir roteiro (problema → solução → dados → modelo → arquitetura)
  - [ ] Preparar slides/visuals
  - [ ] Gravar vídeo (máx 5 minutos)
  - [ ] Incluir demos/screenshots
  - [ ] Fazer upload (YouTube/Drive)
  - [ ] Adicionar link no README
- **Entrega**: Link do vídeo em `README.md`
- **Link**: [GitHub #56](https://github.com/AI-FIAP-2026/farmtech-solutions/issues/56)

#### #57: [Task] Validação Final e Revisão da Entrega
- **Prioridade**: 🔴 Alta
- **Tamanho**: 🔵 Medium (5-8 pts)
- **Responsabilidade**: QA e finalização
- **Dependências**: Todas as tarefas
- **Checklist**:
  - [ ] Verificar completude de arquivos
  - [ ] Validar coerência análise ↔ solução técnica
  - [ ] Revisar clareza e formatação
  - [ ] Confirmar links no README funcionam
  - [ ] Testar acessibilidade do vídeo
  - [ ] Revisão ortográfica final
- **Entrega**: Checklist de validação preenchido
- **Link**: [GitHub #57](https://github.com/AI-FIAP-2026/farmtech-solutions/issues/57)

---

## 📊 Resumo de Métricas

| Métrica | Valor |
|---------|-------|
| **Total de Issues** | 11 (1 Epic + 10 Subtasks) |
| **Issues Type Task** | 10 (90%) |
| **Issues Type Feature** | 1 (10%) |
| **Prioridade Alta** | 7 issues |
| **Prioridade Média** | 4 issues |
| **Tamanho estimado total** | ~80-100 story points |

---

## 🔗 Dependências entre Issues

```
#46 (EPIC PAI)
├─ #47 (Análise Negócio)
│  └─ #48 (Fatores de Risco)
│     ├─ #49 (Dataset)
│     │  └─ #50 (EDA)
│     └─ #51 (Modelo)
│        └─ #52 (Arquitetura)
│           └─ #53 (Integrações)
├─ #54 (Roadmap) 🔄 [paralelo aos análise blocos]
↓
#55 (README) [integra tudo]
└─ #56 (Vídeo)
   └─ #57 (Validação Final)
```

### Caminho Crítico
1. #47 → #48 → #49 → #50 (8-16 pts)
2. #48 → #51 → #52 → #53 (16-20 pts)
3. #54 (paralelo, 8-13 pts)
4. Convergência: #55 (8-13 pts)
5. #56 → #57 (10-16 pts)

---

## 📁 Estrutura de Entrega

```
farmtech-solutions/
├── docs/
│   ├── analise-negocio.md           (#47)
│   ├── fatores-risco.md              (#48)
│   ├── modelo-preditivo.md           (#51)
│   ├── arquitetura.md                (#52)
│   ├── integracao-servicos.md        (#53)
│   ├── analise-exploratoria.md       (#50)
│   ├── roadmap.md                    (#54)
│   ├── sprint-backlog.md             (#54)
│   └── SPRINT1-BACKLOG.md            (este arquivo)
├── data/
│   ├── schema.md                     (#49)
│   ├── dicionario_dados.md           (#49)
│   └── exemplo_dataset.csv           (#49)
├── scripts/
│   └── eda.py                        (#50)
├── assets/
│   ├── arquitetura-sistema.drawio    (#52)
│   └── analise/
│       ├── heatmap-correlacao.png    (#50)
│       ├── distribuicoes.png         (#50)
│       └── ...
└── README.md                         (#55, atualizado)
```

---

## 🚀 Próximos Passos

1. **Hoje**: Revisar e validar estrutura do backlog
2. **Dia 1-2**: Iniciar #47 (Análise Negócio)
3. **Dia 2-3**: Paralelo #48 (Fatores Risco)
4. **Dia 3-4**: #49 (Dataset)
5. **Dia 4-5**: #50 + #51 + #52 (paralelo)
6. **Dia 5-6**: #53 + #54 (paralelo)
7. **Dia 6-7**: #55 (README integrado)
8. **Dia 7-8**: #56 (Vídeo)
9. **Dia 8**: #57 (Validação final)

---

## 📞 Referências

- **Challenge Brief**: [Enterprise Challenge - Sprint 1 - Sompo.md](Enterprise%20Challenge%20-%20Sprint%201%20-%20Sompo.md)
- **GitHub Issues**: https://github.com/AI-FIAP-2026/farmtech-solutions/issues?q=is%3Aopen+is%3Aissue
- **GitHub Project**: https://github.com/orgs/AI-FIAP-2026/projects/1
- **Repositório**: https://github.com/AI-FIAP-2026/farmtech-solutions

---

**Documento gerado automaticamente pela análise de backlog - Sprint 1 Challenge Sompo**
