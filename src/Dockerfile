# Use uma imagem oficial do Python como imagem base
FROM python:3.11-slim

# Evita que o Python gere arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Garante que o Python irá exibir logs diretamente no terminal
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Atualiza o gerenciador de pacotes e instala dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo do projeto para o diretório de trabalho
COPY . .

# Exponha a porta se o seu aplicativo a utilizar (opcional)
# EXPOSE 8000

# Comando para rodar o script Python
CMD ["python", "main.py"]
