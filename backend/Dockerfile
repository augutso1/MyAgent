# 1. Imagem python
FROM python:3.11-slim

# 2. Diretório de trabalho
WORKDIR /app

# 3. Copia dependências
COPY requirements.txt .

# 4. Dependências
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 5. Backend
COPY ./app /app/app

# 6. Porta do Uvicorn
EXPOSE 8000

# 7. Comando para rodar a aplicação quando o contêiner iniciar
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]