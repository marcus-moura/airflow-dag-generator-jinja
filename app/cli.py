"""
CLI that uses Typer to build the command line interface.

python cli.py --help

python -m cli all
python -m cli config_file.yaml
"""
from dag_generator import DAGGenerator
import typer

def main(file_config: str):

    if file_config == "all":
        DAGGenerator().generate_dags()
    else:
        DAGGenerator().generate_dags(file_config)

if __name__=="__main__":
    typer.run(main)