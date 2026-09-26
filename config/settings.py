from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DADOS = os.getenv('BASE_DADOS', default='data_dev/empresas.parquet')