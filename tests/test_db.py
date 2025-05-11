from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

def test_db_user():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("senha_db"),
        database="test_db"
    )
    cursor = conexao.cursor()
    cursor.execute("SELECT nome FROM usuarios WHERE id = 1")
    resultado = cursor.fetchone()
    assert resultado[0] == "João Silva"