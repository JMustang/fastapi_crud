# CRUD com FastAPI e poetry

## Do zero ao CRUD

- Instalando versão do python com **pyenv**

```bash
pyenv update
pyenv install 3.11:latest
```

- Instalando o **poetry** com **pipx**

```bash
pip install pipx
pipx install poetry
```

### Iniciando o projeto

```bash
poetry new nome-do-projeto
cd nome-do-projeto
```

- Esse Comando inicia o projeto e vai criar uma estrutura de pastas parecida com essa

```bash
.
├── nome-do-projeto
│   └──__init__.py
├── poetry.lock
├── README.md
└── pyproject.toml
└── tests
    └──__init__.py
```

- Criando ambiente virtual

```bash
poetry install
```

- Esse comando cria uma pasta chamada **.venv** na raiz do projeto.

```bash
poetry shell
```

- Esse comando inicia o ambiente virtual

```bash
poetry add fastapi
```

- Esse comando instala o **fastapi** no projeto

- Criando uma rota para testa, dentro do diretório raiz crie um arquivo **main.py** e adicione o seguinte código

```py
# main.py
from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def rota_teste():
return {'message': 'Olá Mundo!'}
```

- Para executar precizamos de um servidor, no fastapi e recomendado usar o **uvicorn**

```bash
poetry add uvicorn

# Para executar nossa estrutura
# esse comando inicia o servidor apontando para o arquivo main.py
uvicorn nome-do-projeto.main:app --reload --host localhost --port 8000
```

No seu navegador digite **http://localhost:8000**
