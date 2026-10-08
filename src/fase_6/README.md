# Fase 6 - Cap 1 - O despertar da Rede Neural

## Identificação

**Fase:** 6
**Capítulo:** 1
**Grupo:** H.M.N.R.V.
**Entregável:** 1 e 2

---

## Descrição da Atividade

O projeto tem como objetivo utilizar técnicas de **Visão Computacional e Deep Learning** para reconhecer objetos em imagens, trabalhando com **duas classes** (Copo e Taça).

O desafio consiste em preparar e validar o conjunto de imagens (treino, validação e teste), treinar uma **YOLOv5 customizada** com diferentes números de épocas, comparar seu desempenho com uma **YOLO pré-treinada** (sem customização) e com uma **CNN criada do zero**, avaliando precisão, tempo de treinamento e facilidade de uso de cada abordagem.

---

## Bibliotecas Utilizadas

As principais bibliotecas utilizadas no projeto são:

* **YOLOv5 (Ultralytics)** — detecção de objetos (treinamento, validação e inferência);
* **TensorFlow / Keras** — construção e treinamento da CNN do zero;
* **Pandas** — manipulação e organização dos resultados;
* **Matplotlib e Seaborn** — gráficos, curvas de aprendizado e matriz de confusão;
* **Scikit-learn** — métricas de avaliação (matriz de confusão);
* **PyYAML** — leitura do arquivo de configuração do dataset.

Entre as abordagens comparadas estão **YOLOv5 customizada (20 e 40 épocas), YOLOv5s pré-treinada (COCO) e CNN criada do zero**.

---

## Estrutura do Repositório

```
src/fase6/
    cnn.ipynb
    datasets/
        CNN/                (imagens organizadas em train, val e test)
        RedeNeuralYolo/     (imagens, rótulos e classificar.yaml)
```

A pasta `datasets` é equivalente à pasta **Cap 1 - O despertar da Rede Neural** utilizada originalmente no Google Drive.

---

## Como Executar o Notebook

O notebook foi desenvolvido para ser executado no **Google Colab** e lê os dados diretamente do **Google Drive**. Para executá-lo corretamente, siga os passos abaixo:

### 1. Baixe os arquivos

Faça o download, neste repositório, de:

* o notebook `cnn.ipynb`;
* a pasta `datasets` completa (com as subpastas `CNN` e `RedeNeuralYolo`).

### 2. Suba os dados para o seu Google Drive

No seu Google Drive, crie a pasta **`Cap 1 - O despertar da Rede Neural`** dentro de **Meu Drive** e envie para ela o conteúdo da pasta `datasets`, de forma que fique assim:

```
Meu Drive/
    Cap 1 - O despertar da Rede Neural/
        CNN/
        RedeNeuralYolo/
```

> Os nomes das pastas devem ser mantidos exatamente como acima, pois o notebook usa esses caminhos (`/content/drive/MyDrive/Cap 1 - O despertar da Rede Neural/...`).

### 3. Abra o notebook no Google Colab

Acesse o [Google Colab](https://colab.research.google.com), faça o upload do arquivo `cnn.ipynb` e ative a **GPU** em *Ambiente de execução > Alterar tipo de ambiente de execução* (o treinamento da CNN utiliza a GPU).

### 4. Execute as células

Execute as células do notebook **na ordem em que aparecem**, começando pela primeira e seguindo até a conclusão. Na primeira execução, o Colab solicitará autorização para acessar o seu Google Drive.

O treinamento das YOLOs leva, aproximadamente, **17 minutos (20 épocas)** e **33 minutos (40 épocas)**.

---

## Integrantes

* Heitor Exposito de Sousa - RM 566013
* Marco Antônio Rodrigues Siqueira - RM 569975
* Nádia Nakamura Vieira - RM 568906
* Rafael Bassani - RM 569930
* Vinicius Xavier da Silva - RM 572108

---

## Métodos Utilizados

### Validação do Dataset

O dataset possui **duas classes** e é dividido em treino, validação e teste. O notebook valida, para cada divisão, a quantidade de imagens, a quantidade de imagens por classe e a existência dos arquivos de rótulo no formato YOLO. A rotulagem foi realizada na ferramenta **Make Sense**.

### YOLOv5 Customizada

Foi utilizada a **YOLOv5s** com pesos pré-treinados como ponto de partida (transferência de aprendizado), treinada com as duas classes do projeto. Foram realizados dois experimentos com os mesmos parâmetros, alterando somente o número de épocas (**20 e 40**). Os modelos são avaliados pelas métricas **Precision, Recall e mAP**, além da matriz de confusão e das curvas geradas pelo YOLO.

### YOLOv5 Pré-treinada

A **YOLOv5s** original, treinada no dataset COCO e **sem treinamento nas classes do projeto**, foi executada sobre as mesmas imagens de teste para análise qualitativa. Como o modelo reconhece apenas as classes do COCO, ele pode não identificar as classes do trabalho.

### CNN Criada do Zero

Foi construída uma CNN com **TensorFlow/Keras**, composta por camada de reescala, convolução, max pooling e camadas densas, com saída sigmoid para classificação binária. O treinamento utiliza **Early Stopping** e o modelo é avaliado pela **acurácia** e pela **matriz de confusão** no conjunto de teste.

> A YOLO resolve um problema de **detecção de objetos** (classe e localização), enquanto a CNN resolve um problema de **classificação**. Por isso, **mAP** e **acurácia** não são métricas diretamente comparáveis.

---

## Conclusões

A análise permitiu comparar diferentes abordagens de Visão Computacional para o reconhecimento das duas classes do projeto.

Entre os modelos avaliados, a **YOLOv5 customizada treinada por 40 épocas apresentou o melhor desempenho**, com **mAP@0.5 de 0,99**, contra **0,78** do treinamento de 20 épocas. Em contrapartida, o tempo de treinamento dobrou (de cerca de 17 para cerca de 33 minutos).

A **YOLO pré-treinada** não foi avaliada por métrica numérica, já que foi treinada no COCO e não nas classes deste trabalho. A **CNN criada do zero** obteve **acurácia de 72% no teste**, funcionando como classificador e não como detector.

O projeto evidencia que a escolha da arquitetura depende do problema: modelos de detecção como a YOLO fornecem classe e localização do objeto, enquanto uma CNN classificadora é adequada quando o objeto já está isolado na imagem.
## Vídeos Demonstrativos

### Entregável 1

[Assista ao vídeo demonstrativo 1 no YouTube](youtube.com/watch?v=v5UiTAw8Jhc&feature=youtu.be)
[Acesse o Notebook no Google Colab](https://colab.research.google.com/drive/1Y-jDRm9pqECWsGKeNOTVH8ZvC7s0NgoW?usp=sharing)

### Entregável 2

[Assista ao vídeo demonstrativo 2 no YouTube]()
[Acesse o Notebook no Google Colab](https://colab.research.google.com/drive/1Y-jDRm9pqECWsGKeNOTVH8ZvC7s0NgoW?usp=sharing)

---

## Arquivos

* `MarcoSiqueira_rm569975_pbl_fase6_entrega1&2_unificada.ipynb` — Notebook contendo o desenvolvimento do projeto.
* `/Cap 1 - O despertar da Rede Neural` — Dataset utilizado na atividade.

---