import os

# Настройки базы данных
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://admin:admin@localhost/sa')

# Настройки приложения
DEBUG = False
ALLOWED_HOSTS = ['*'] 