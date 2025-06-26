# 1. Fase de Build
FROM node:18-alpine AS builder

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de definição de pacotes
COPY package*.json ./

# Instala as dependências
RUN npm install

# Copia o resto do código do frontend
COPY . .

# Roda o comando de build do Next.js
RUN npm run build

# 2. Fase de Produção: Usamos uma imagem Node.js menor para rodar a aplicação já construída
FROM node:18-alpine

WORKDIR /app

# Copia a pasta 'node_modules' da fase de build
COPY --from=builder /app/node_modules ./node_modules

# Copia a pasta '.next' (que contém a aplicação otimizada) da fase de build
COPY --from=builder /app/.next ./.next

# Copia o 'package.json' e o 'public'
COPY package.json .
COPY public ./public

# Expõe a porta 3000
EXPOSE 3000

# Iniciar o servidor Next.js em modo de produção
CMD ["npm", "start"]