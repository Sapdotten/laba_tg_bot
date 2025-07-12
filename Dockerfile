# Используем базовый образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем все содержимое текущей директории в рабочую директорию контейнера
COPY . .


# Копируем файл .env
#COPY .env ./app/.env

CMD ["python3", "src/main.py"]