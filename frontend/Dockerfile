
# Используем официальный образ Node.js
FROM node:20 AS build

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и устанавливаем зависимости
COPY package.json ./
RUN npm install

# Копируем все файлы и собираем проект
COPY . ./
ENV NODE_OPTIONS="--openssl-legacy-provider"
RUN npm run build

# Статический сервер для обслуживания build-версии React
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
