import os

db_URI = os.getenv('DATABASE_URL', 'postgresql://localhost:5432/videohub_db')
secret = os.getenv('SECRET', 'Oh my god they were roommates.')
