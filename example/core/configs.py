"""
Generated by Panther
"""

from pathlib import Path
from dotenv import dotenv_values
from sqlalchemy.orm import declarative_base




DEBUG = True  # DEBUG is default False (You Can Remove It)
BASE_DIR = Path(__name__).resolve().parent
env = dotenv_values(BASE_DIR / '.env')

# Load Env Variables

DB_NAME = env['DB_NAME']
DB_HOST = env['DB_HOST']
DB_PORT = env['DB_PORT']
SECRET_KEY = env['SECRET_KEY']
DB_USERNAME = env['DB_USERNAME']
DB_PASSWORD = env['DB_PASSWORD']


# # Go To https://framework.org/Middlewares For More Options
Middlewares = [
    'panther/middlewares/db.py'
]

# # Go To https://framework.org/Authentications For More Options
# Authentication = JWTAuthentication
#
# # Only If Authentication Set To JWT
# JWTConfig = {
#     'Algorithm': 'HSA256',
#     'TokenLifeTime': timedelta(days=2),
#     'Key': SECRET_KEY
# }


# Go To https://framework.org/SupportedDatabase For More Options
# DATABASE = postgresql
DatabaseConfig = {
    'DATABASE_TYPE': 'SQLite',
    'NAME': DB_NAME,
    'HOST': DB_HOST,
    'PORT': DB_PORT,
    'USERNAME': DB_USERNAME,
    'PASSWORD': DB_PASSWORD,
}


URLs = 'core/urls.py'
