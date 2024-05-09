# Usar a imagem oficial do Python como a base
FROM python:3.11.7

# Definir variáveis ​​de ambiente para evitar problemas de codificação
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /Incomum3.0-main

# Instalar as dependências do sistema
RUN apt-get update && apt-get install -y \
    postgresql-client

# Copiar o arquivo requirements.txt e instalar as dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o diretório do aplicativo para o diretório de trabalho no contêiner
COPY . /app/

# Expor a porta em que o aplicativo Django será executado
EXPOSE 8000
# Comando para iniciar o servidor de desenvolvimento do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
