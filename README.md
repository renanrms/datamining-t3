# Bus time and location prediction

Curso: Mestrado em Engenharia de Sistemas e Computação
Disciplina: Data Mining
Professor: Zimbrão

O desafio deste trabalho é prever a localização de um ônibus em dado horário ou horário para uma data localização.

## Fonte dos dados

- [Treino](https://drive.google.com/drive/folders/1Sc3vwxvNFRc3lFxlLXwwF4QoHGYePdRI)
- [Teste](https://drive.google.com/drive/folders/1Bt3F7QUTKt7ksxy55vOWM_DtrgxqUh2N)
- [final](https://drive.google.com/drive/folders/1rYjhZ2xf_gmfCzOaNPAprcImX8yYP5B3)

## Como executar a análise

### Preparação do banco de dados

```
sudo docker compose up
```

### Preparação do ambiente Python

Certifique-se de ter o Pyhton e o Pypi instalados.

Instale o [Python Dependency Manager (PDM)](https://pdm-project.org/en/latest/):

```
pip install pdm
```

Instale as dependências do projeto (será criado um ambiente virtual Python apenas para o projeto):

```
pdm install
```

### Execução

Abra o arquivo Jupyter Notebook, `solution.py` e o execute. Ele deve estar apontando para o ambiente local.
