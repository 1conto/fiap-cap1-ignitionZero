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

### 🧠 Técnicas utilizadas no projeto
Durante a construção da solução, foram aplicadas algumas técnicas importantes:

- **Simulação com aleatoriedade (`random`)**: os dados de telemetria são gerados com funções aleatórias para representar cenários reais e imprevisíveis de operação.
- **Validação por regras (rule-based validation)**: os valores capturados são comparados com limites pré-definidos no dicionário `valores_seguros`.
- **Auditoria de falhas**: além de validar, o código registra o motivo da falha para facilitar análise e tomada de decisão antes da decolagem.
- **Separação de responsabilidades**: cada classe/função tem um papel específico, melhorando organização, leitura e manutenção.

### 🧱 Uso das classes
O projeto utiliza **Programação Orientada a Objetos (POO)** para representar entidades do cenário:

- **Classe `ModulosCriticos`**: representa um módulo crítico individual (ex.: navegação, comunicação), com seu nome e status de funcionamento.
- **Classe `Telemetria`**: centraliza a coleta dos dados dos sensores, testes dos módulos e execução das validações.

Essa abordagem com classes ajuda a:

- agrupar dados e comportamentos relacionados;
- facilitar reuso e expansão (ex.: novos sensores/módulos);
- manter o código mais limpo do que concentrar tudo em blocos soltos.

### ⚙️ Motivo das funções principais
As funções/métodos foram criados para reproduzir o fluxo real de um checklist de pré-decolagem:

- **`captura_*`**: simular leituras de sensores individuais;
- **`testar_todos_modulos()`**: validar rapidamente o estado dos sistemas essenciais;
- **`captura_todas_infos()`**: consolidar a coleta em uma única chamada;
- **`validacoes_telemetria()`**: aplicar as regras de segurança e gerar validação + auditoria;
- **`valida_decolagem()`**: apresentar o resultado final de forma clara para decisão operacional.

---

## 🖼️ Prints da execução
Nesta seção você pode adicionar os prints reais da execução após rodar o código.

---

## ▶️ Instruções de execução do código
### Pré-requisitos
- Python **3.10+**

### Opção 1: Executar via Jupyter Notebook
1. Abra o arquivo `main.ipynb` no VS Code (com extensão Jupyter) ou Jupyter Lab.
2. Execute as células em ordem, do topo até a célula `valida_decolagem(valida, auditoria)`.
3. Verifique a saída no final do notebook.

### Opção 2: Executar via script Python
Caso prefira terminal, você pode copiar a lógica do notebook para um arquivo `.py` e executar:

```bash
python nome_do_arquivo.py
```

> Observação: o projeto usa geração aleatória de valores, então os resultados podem mudar a cada execução.
