# 🚀 FIAP CAP1 - Ignition Zero

Simulação de um **relatório operacional de pré-decolagem** para missão espacial, desenvolvida em Python no notebook `main.ipynb`.

---

## 📖 Visão geral
O projeto representa um checklist de segurança antes da decolagem.
A cada execução, valores de telemetria são simulados e comparados com regras de segurança para decidir se a missão está:

- ✅ **Pronta para decolar** (`Pronto para Decolar!`)
- ❌ **Reprovada para decolagem** (`Falha na decolagem!`), com motivos de falha

---

## 🎯 Objetivo acadêmico
Aplicar fundamentos de lógica e Python em um cenário prático, com foco em:

- modelagem de domínio;
- validação de regras;
- estruturação orientada a objetos;
- geração de saída interpretável para apoio à decisão.

---

## 🧠 Técnicas utilizadas

### 1) Simulação estocástica (aleatoriedade)
A biblioteca `random` gera medições e estados dos módulos para representar variação real de operação.

### 2) Validação orientada a regras
As regras de segurança ficam centralizadas no dicionário `valores_seguros`, com limites mínimos/máximos ou estado booleano esperado.

### 3) Auditoria operacional
Além de validar, o sistema retorna justificativas de falha para cada item fora da conformidade, facilitando diagnóstico.

### 4) Programação orientada a objetos (POO)
O domínio foi dividido em classes para separar responsabilidades e tornar o fluxo mais legível e escalável.

---

## 🏗️ Estrutura lógica (classes e responsabilidades)

### `ModulosCriticos`
Representa um módulo crítico do foguete (ex.: comunicação, navegação, propulsão), contendo:
- nome do módulo;
- status de saúde (`True`/`False`) após teste.

### `Telemetria`
Centraliza o fluxo operacional:
- captura dados de sensores;
- testa todos os módulos críticos;
- executa validações comparando medições com `valores_seguros`;
- produz resultado final de validação e auditoria.

---

## ⚙️ Motivo das funções principais

- **`captura_*`**: simulam leituras unitárias de telemetria.
- **`testar_todos_modulos()`**: verifica rapidamente a saúde dos sistemas essenciais.
- **`captura_todas_infos()`**: orquestra a coleta completa de dados em uma única chamada.
- **`validacoes_telemetria()`**: aplica as regras de segurança e monta o relatório (validação + auditoria).
- **`valida_decolagem()`**: comunica decisão final de forma direta para operação.

---

## 🗂️ Estrutura do repositório

```text
.
├── main.ipynb   # Notebook com toda a implementação da simulação
└── README.md    # Documentação do projeto
```

---

## ▶️ Como executar

### Pré-requisitos
- Python **3.10+**
- Ambiente com suporte a Jupyter Notebook (VS Code + extensão Jupyter, Jupyter Lab ou Colab)

### Opção 1 — Notebook (recomendado)
1. Abra `main.ipynb`.
2. Execute as células em ordem.
3. Observe o resultado final na célula com `valida_decolagem(valida, auditoria)`.

### Opção 2 — Script Python
Se desejar, converta/copie a lógica para um arquivo `.py` e execute:

```bash
python nome_do_arquivo.py
```

> ℹ️ Como os dados são aleatórios, os resultados mudam entre execuções.

---

## 🖼️ Prints da execução
Adicione aqui os prints reais da execução após rodar o notebook.

Exemplo de organização sugerida:
- `assets/execucao-ok.png`
- `assets/execucao-falha.png`

---

## 🔮 Melhorias futuras
- exportar relatório de auditoria para JSON/CSV;
- adicionar testes automatizados para validações;
- criar versão em script CLI com parâmetros de simulação;
- incluir métricas históricas de falhas por módulo.

---

## 👨‍💻 Autor
Projeto acadêmico FIAP — Capítulo 1.
