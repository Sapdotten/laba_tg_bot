# Используем базовый образ Python
FROM python:3.10.12

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все содержимое текущей директории в рабочую директорию контейнера

COPY . .

# Копируем файл .env
COPY .env .env

# Открываем порт, который будет использоваться для запуска приложения
EXPOSE 8080

# Запускаем приложение с помощью uvicorn
CMD ["uvicorn app.app:app --host 0.0.0.0 --port 5000 --reload &", "python3 app/main.py &"]