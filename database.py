import sqlite3

DB_NAME = "study-manager.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS materias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            materia_id INTEGER,
            status TEXT DEFAULT 'pendente',
            propridade TEXT DEFAULT 'media',
            FOREIGN KEY (materia_id) REFERENCES materias(id)
        )
    ''')

    conexao.commit()
    conexao.close()
    