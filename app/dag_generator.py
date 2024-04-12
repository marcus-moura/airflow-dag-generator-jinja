from jinja2 import Environment, FileSystemLoader
import yaml
import os
from pathlib import Path
from loguru import logger
import sys

# Configuração do log
logger.remove()
logger.add(sys.stdout, colorize=True, format="<green>{time:YYYY-MM-DD at HH:mm:ss}</green> | {level} | {message}")
logger.level("INFO")

class DAGGenerator:
    def __init__(self,
                 templates_dir: str = "templates", 
                 configs_dir: str = "configs", 
                 output_dir: str = "dags",
                 project_dir: str = None
        ):
        if project_dir:
            self.project_dir = Path(project_dir)
        else:
            # Se o diretório do projeto não for fornecido, use o diretório do script atual
            self.project_dir = Path(__file__).resolve().parent

        self.templates_dir = self.project_dir / templates_dir
        self.configs_dir = self.project_dir / configs_dir
        self.output_dir = self.project_dir / output_dir

    def generate_dags(self, file_config: str = None):

        # Carrega o ambiente do Jinja2
        env = Environment(loader=FileSystemLoader(str(self.templates_dir)))
        
        if file_config:
            # Gera uma única DAG a partir do arquivo de configuração especificado
            config_file_path = self.configs_dir / file_config
            self._generate_dag_from_config(env, config_file_path)
        else:
            # Gera DAGs para todos os arquivos de configuração no diretório de configurações
            for file_name in os.listdir(self.configs_dir):
                if file_name.endswith('.yaml'):
                    config_file_path = self.configs_dir / file_name
                    self._generate_dag_from_config(env, config_file_path)

    def _generate_dag_from_config(self, env, config_file_path):
        try:
            with open(config_file_path, "r") as config_file:
                configs = yaml.safe_load(config_file)
            
            # Renderiza o template Jinja2
            template = env.get_template(str(configs['template']))
            output_file = template.render(configs)
            
            # Escreve o arquivo de saída da DAG
            output_filename = f"{configs['dag']['dag_id']}.py"
            output_file_path = self.output_dir / output_filename
            with open(output_file_path, "w") as f:
                f.write(output_file)
                
            logger.info(f"DAG {output_filename} successfully generated for {config_file_path}.")
        except FileNotFoundError:
            logger.error(f"File Not Found: {config_file_path}")
        except Exception as e:
            logger.error(f"Error generating DAG from {config_file_path}: {e}")
