# Используем базовый образ Python
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей в рабочую директорию
COPY requirements.txt requirements.txt

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем все содержимое текущей директории в рабочую директорию контейнера

COPY . .

# Копируем файл .env
#COPY .env ./app/.env

# Открываем порт, который будет использоваться для запуска приложения
EXPOSE 8080

# Запускаем приложение с помощью uvicorn
CMD ["sh", "-c", "uvicorn app.app:app --host 0.0.0.0 --port 8080 --reload & python3 app/main.py &"]