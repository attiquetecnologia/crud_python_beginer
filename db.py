# conexão com banco de dados

import sqlite3

# conecta ao banco de dados 'todo-app'
# caso o banco não exista ele será criado
conn = sqlite3.connect("databse.db")

def create_database():
    """ cria a tabela 'tarefa' caso ela não exista """
    cursor = conn.cursor()
    conn.execute("""
    create table if not exists tarefa (
        id integer primary key autoincrement,
        tarefa text,
        concluido integer
    )
    """)

