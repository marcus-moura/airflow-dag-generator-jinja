# Genador de DAGs com Templates Jinja

## Descrição
O projeto consiste em um sistema de geração de DAGs (Directed Acyclic Graphs) para o Apache Airflow, uma plataforma de orquestração de fluxo de trabalho. A geração das DAGs é feita usando modelos Jinja2 e configurações YAML.

### Funcionalidades

- **Geração Dinâmica de DAGs:** Crie DAGs dinamicamente com base em modelos Jinja2 e configurações YAML.
- **Estrutura de Diretórios Flexível:** Lida facilmente com uma estrutura flexível de diretórios, permitindo a organização de arquivos em diferentes subdiretórios.
- **Configuração Centralizada:** As configurações das DAGs são definidas em arquivos YAML para uma configuração centralizada e fácil personalização.
- **Geração Automatizada:** Pode ser integrado a pipelines de CI/CD para automatizar a geração de DAGs em diferentes ambientes.

### Componentes

- **DAG Generator:** Classe responsável por gerar as DAGs com base nos modelos Jinja2 e configurações YAML fornecidos.
- **Templates Jinja2:** Definem a estrutura das DAGs, incluindo tarefas, dependências e outros parâmetros configuráveis.
- **Configurações YAML:** Contêm as configurações específicas de cada DAG, como nome, cronograma de execução e parâmetros de tarefas.
- **CLI (Command Line Interface):** Fornece uma interface de linha de comando para interagir com o sistema de geração de DAGs. O arquivo cli.py contém os comandos disponíveis para gerar DAGs.

## Estrutura do Projeto

```bash
├── app/
│   ├── configs/
│   │   ├── config_dag_exemple_1.yaml
│   │   ├── config_dag_exemple_2.yaml
│   ├── dags/
│   │   ├── dag_template_exemple_1.py
│   │   ├── dag_template_exemple_2.py
│   ├── templates/
│   │   ├── dag_template.jinja2
│   ├── __init__.py/
│   ├── cli.py/
│   ├── dag_generator/
├── .gitignore
├── .python-version
├── poetry.lock
├── pyproject.toml
├── requirements.txt
└── README.md
``````

## Requisitos

Certifique-se de ter os seguintes pré-requisitos instalados:

- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/docs/)

## Instalação
Para a instalação do projeto, siga as instruções abaixo:

1. Clone o repositório:

    ```bash
    git clone https://github.com/marcus-moura/airflow-dag-generator-jinja.git
    ```
2. Navegue até o diretório do projeto recém-clonado:

    ```bash
    cd airflow-dag-generator-jinja
    ```
### Utilizando `pip`

Se você preferir usar o `pip` para instalar as dependências, siga estas etapas:

1. **Criação e Ativação do Ambiente Virtual Python:**

    - No Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

    - No Windows:
        ```bash
        python3 -m venv venv
        .\venv\Scripts\activate
        ```

2. **Instalação dos Pacotes Python Necessários:**

    Execute os seguintes comandos para instalar os pacotes listados nos arquivos `requirements.txt`

    ```bash
    pip install -r requirements.txt
    ```

### Utilizando Poetry

Se você preferir usar o gerenciador de pacotes Poetry, siga estas etapas:

1. **Instalação das Dependências com Poetry:**

    Instale as dependências do projeto usando Poetry:

    ```bash
    poetry install
    ```

2. **Ativação do Ambiente Virtual:**

    Ative o ambiente virtual criado pelo Poetry:

    ```bash
    poetry shell
    ```
## Configuração
1. **Defina seus Templates:** Crie templates Jinja2 para suas DAGs com as tarefas e dependências desejadas.
2. **Configure suas DAGs:** Especifique as configurações de cada DAG em arquivos YAML no diretório `configs`.

## Uso

Para executar o gerador de DAGs acesse o diretório `app` e execute a CLI.

### Comandos CLI

O arquivo `cli.py` fornece uma interface de linha de comando para interagir com o gerador de DAGs. Aqui estão alguns comandos disponíveis:

- **Gerar todas DAGs:** Use o comando `python -m cli all` para gerar todas as DAGs disponíveis no diretório `configs` com base nos templates Jinja2.
- **Listar DAGs:** Use o comando `python -m cli {config_file_name}.yaml` para gerar uma dag com base em um arquivo de configuração específico.

Certifique-se de ter todas as dependências instaladas e as configurações corretamente definidas antes de usar os comandos CLI.

## Contato

Se você tiver dúvidas ou sugestões, entre em contato comigo em marcuspaulo.moura@hotmail.com.

## Links Úteis

- [Python](https://www.python.org/)
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)

