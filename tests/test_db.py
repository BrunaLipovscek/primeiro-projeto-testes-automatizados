import mysql.connector

def test_db_user():
    conexao = mysql.connector.connect(
        host="local host",
        user="root",
        password="senha_db",
        database="test_db"
    )
    cursor = conexao.cursor()
    cursor.execute("SELECT nome FROM usuarios WHERE id = 1")
    resultado = cursor.fetchone()
    assert resultado[0] == "João Silva"