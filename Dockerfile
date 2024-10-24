# Usando uma imagem base do Python
FROM python:3.10-slim

# Configurando o diretório de trabalho
WORKDIR /app

# Copiando os arquivos de requirements e instalando as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o resto do código
COPY . .

# Expondo a porta que o Flask vai rodar
EXPOSE 5000

# Comando para iniciar o Flask
CMD ["flask", "run", "--host=0.0.0.0"]
