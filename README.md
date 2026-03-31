# FIAP CAP1 - Ignition Zero

## 📌 Explicação do projeto
Este projeto simula um **relatório operacional de pré-decolagem** de uma missão espacial.
A lógica principal está no notebook `main.ipynb`, onde são modelados:

- **Módulos críticos da aeronave/foguete** (computador de voo, navegação, comunicação etc.);
- **Sensores de telemetria** (temperatura interna/externa, pressão do tanque, nível de energia e integridade estrutural);
- **Regras de segurança** (`valores_seguros`) para validar se a decolagem pode ser autorizada.

Ao executar a validação, o sistema compara os valores capturados com os limites seguros e imprime:

- `Pronto para Decolar!` quando tudo está dentro da conformidade;
- `Falha na decolagem!` com os motivos de reprovação quando algum item está fora do padrão.

---

## 🧭 Fluxograma da lógica do código

```mermaid
flowchart TD
    A[Início] --> B[Definir lista de módulos críticos]
    B --> C[Criar classe ModulosCriticos]
    C --> D[Criar classe Telemetria]
    D --> E[Instanciar Telemetria com módulos]
    E --> F[Definir valores_seguros]
    F --> G[Executar validacoes_telemetria]

    G --> G1[Testar status de todos os módulos]
    G1 --> G2[Capturar dados de telemetria\nTemp interna/externa\nIntegridade\nNível bateria\nPressão tanque]
    G2 --> G3[Para cada regra em valores_seguros]

    G3 --> H{Tipo da regra}
    H -->|modulos| H1[Validar se todos módulos estão OK]
    H -->|faixa min/max| H2[Validar limite numérico]
    H -->|booleano| H3[Validar igualdade booleana]
    H1 --> I[Salvar validações, auditoria e valores]
    H2 --> I
    H3 --> I

    I --> J[Capturar infos de energia\nVoltagem, corrente,\ncapacidade, carga,\nenergia disponível e perda]
    J --> K[Executar valida_decolagem]
    K --> L{Todas validações são True?}
    L -->|Sim| M[PRONTO PARA DECOLAR]
    L -->|Não| N[DECOLAGEM ABORTADA]
    M --> O[Retornar dict final com decisão e motivos]
    N --> O
    O --> P[Fim]
```

### Ordem de leitura
1. **Coleta**: módulos e sensores geram dados simulados.
2. **Validação**: cada dado é comparado com `valores_seguros`.
3. **Auditoria**: o sistema registra regra, valor atual e motivo.
4. **Decisão**: se tudo estiver conforme, decola; caso contrário, aborta.

---

## ▶️ Instruções de execução do código
### Pré-requisitos
- Python **3.10+**

### Opção 1: Executar via Jupyter Notebook
1. Abra o arquivo `main.ipynb` no VS Code (com extensão Jupyter) ou Jupyter Lab.
2. Execute todas as células.
3. Verifique as saídas ao longo do notebook.


### Opção 2: Executar via script Python
Caso prefira terminal, você pode copiar a lógica do notebook para um arquivo `.py` e executar:

```bash
python nome_do_arquivo.py
```

> ℹ️ Como os dados são aleatórios, os resultados mudam entre execuções.

---

## 🖼️ Prints da execução  

Os prints da execução bem sucedida do código, está presente no arquivo PDF. Também é possível executar o código no Notebook Python e executar todas as células no notebook.

---

## 🔮 Melhorias futuras
- exportar relatório de auditoria para JSON/CSV;
- adicionar testes automatizados para validações;
- criar versão em script CLI com parâmetros de simulação;
- incluir métricas históricas de falhas por módulo.

---

## 👨‍💻 Autores
Projeto acadêmico FIAP — Capítulo 1.
### Luis Gustavo Ribeiro Andrade
    Formado em Economia pela FGV EPGE, trabalhou com modelos de Machine Learning ao longo da sua graduação. 
    Os modelos de Machine Learning apresentados no trabalho foram desenvolvidos com seu conhecimento prévio em Econometria e Estatística concedido pela sua graduação anterior.


> Observação: o projeto usa geração aleatória de valores, então os resultados podem mudar a cada execução.
