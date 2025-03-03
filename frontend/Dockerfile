# Используем официальный образ Node.js
FROM node:20 AS build

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install
# Копируем остальные файлы проекта
COPY . .

# Собираем проект
RUN npm run build

# Используем Nginx для раздачи статических файлов
FROM nginx:alpine

# Копируем файлы сборки в Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Открываем порт
EXPOSE 80

# Запускаем Nginx
CMD ["nginx", "-g", "daemon off;"]
