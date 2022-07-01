from starlette.config import Config
import hashlib

config = Config('.conf')

DATABASE_URL = config("DATABASE_URL",cast=str)

def hash_password(password: str) -> str:
    "Хеширование пароля"
    return hashlib.md5(password.encode()).hexdigest()
