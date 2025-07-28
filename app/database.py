from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def debug():
    print("Banco conectado.")

