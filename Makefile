# Variáveis para facilitar a manutenção
PYTHON = python
MAIN_FILE = main.py
PORT = 8000

# Comando padrão (roda se você digitar apenas 'make' no terminal)
all: run

# Comando para instalar as dependências
install:
	pip install fastapi uvicorn sqlalchemy pymysql

# Comando principal para rodar a API
start:
	$(PYTHON) -m uvicorn main:app --reload --host 0.0.0.0 --port $(PORT)

# Comando para limpar arquivos temporários do Python (opcional)
clean:
	rm -rf __pycache__ .pytest_cache