# Detecção de Anomalias em Dados Financeiros

Este projeto tem como objetivo detectar anomalias em dados financeiros utilizando dois métodos de aprendizado de máquina: **Isolation Forest** e **Local Outlier Factor (LOF)**. O código foi desenvolvido com a biblioteca **Streamlit** para fornecer uma interface web simples, permitindo o carregamento de arquivos Excel e a visualização de resultados.

## Funcionalidades

- **Carregamento de Arquivo Excel**: O usuário pode carregar um arquivo Excel contendo dados financeiros.
- **Detecção de Anomalias**: O modelo aplica os algoritmos **Isolation Forest** e **LOF** para identificar anomalias nos dados.
- **Avaliação do Modelo**: O modelo é avaliado com base em métricas como **Acurácia**, **Precisão** e **Recall**.
- **Matriz de Confusão**: A matriz de confusão é gerada para mostrar os resultados da detecção de anomalias.
- **Visualização das Anomalias**: Exibição gráfica da distribuição das anomalias detectadas.
- **Download de Resultados**: O usuário pode baixar um arquivo Excel contendo as anomalias detectadas.

## Estrutura do Código

- **load_data()**: Carrega o arquivo Excel, remove colunas irrelevantes e seleciona apenas as colunas numéricas.
- **detect_anomalies()**: Aplica os modelos **Isolation Forest** e **LOF** para identificar as anomalias.
- **evaluate_model()**: Avalia a performance do modelo utilizando **Acurácia**, **Precisão**, **Recall** e gera a **Matriz de Confusão**.
- **Streamlit**: Interface web para interagir com o usuário, carregar arquivos, visualizar resultados e baixar o arquivo corrigido.

---

## Como Rodar o Projeto

### Passo 1: Criar o Ambiente Virtual

É altamente recomendado criar um ambiente virtual para garantir que as dependências do projeto não interfiram com outras bibliotecas no seu sistema.

1. **Criar um Ambiente Virtual**:

   No terminal, dentro do diretório do projeto, execute o seguinte comando:

   ```bash
   python -m venv venv
   ```

2. **Ativar o Ambiente Virtual**:

   - No **Windows**, use:
     ```bash
     venv\Scripts\activate
     ```
   - No **Mac/Linux**, use:
     ```bash
     source venv/bin/activate
     ```

   Após ativar o ambiente virtual, você verá algo como `(venv)` no início da linha de comando.

### Passo 2: Instalar as Dependências

1. **Instalar as Dependências**:

   Com o ambiente virtual ativado, instale as bibliotecas necessárias para o projeto com o comando:

   ```bash
   pip install -r requirements.txt
   ```

### Passo 3: Rodar o Aplicativo Streamlit

1. Após instalar todas as dependências, você pode rodar o aplicativo Streamlit com o seguinte comando:

   ```bash
   streamlit run app.py
   ```

   Onde `app.py` é o nome do arquivo contendo o código principal do Streamlit (você pode usar qualquer nome de arquivo desejado, desde que seja o arquivo correto).

2. O Streamlit abrirá automaticamente o navegador e carregará a interface onde você pode carregar o arquivo Excel e começar a detectar as anomalias.

---

## Como Usar o Aplicativo

1. **Carregar Arquivo**: Clique no botão "Carregar arquivo Excel" para selecionar o arquivo desejado.
2. **Detectar Anomalias**: Após carregar o arquivo, clique no botão "🔍 Detectar Anomalias" para aplicar os algoritmos **Isolation Forest** e **LOF**.
3. **Avaliar Resultados**:
   - Visualize as **Anomalias Detectadas**.
   - Veja as métricas de **Acurácia**, **Precisão**, **Recall** e a **Matriz de Confusão**.
4. **Visualização**: O gráfico de **Distribuição das Anomalias** será exibido mostrando a frequência das anomalias detectadas.
5. **Download dos Resultados**: Após a detecção, um arquivo Excel com os resultados estará disponível para download.

---

## Estrutura do Projeto

```
detecao_anomalias/
├── app.py                # Código principal do Streamlit
├── requirements.txt      # Arquivo de dependências
├── venv/                 # Ambiente virtual
├── data/                 # Diretório para dados (opcional)
└── README.md             # Este arquivo
```

