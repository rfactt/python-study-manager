from database import conectar 
from models import status_valido, prioridade_valida

def cadastrar_materia(nome):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("INSERT INTO materias (nome) VALUES (?)", (nome,))
        conexao.commit()
        print("Matéria cadastrada com sucesso.")
    except Exception as erro:
        print(f"Erro ao cadastrar matéria: {erro}")
    finally:
        conexao.close()


def listar_materias():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM materias")
    materias = cursor.fetchall()

    conexao.close()
    return materias


def cadastrar_tarefa(titulo, materia_id, prioridade):
    if not prioridade_valida(prioridade):
        print("Prioridade inválida. Use: baixa, media ou alta.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO tarefas (titulo, materia_id, prioridade)
            VALUES (?, ?, ?)
        """, (titulo, materia_id, prioridade))

        conexao.commit()
        print("Tarefa cadastrada com sucesso.")

    except Exception as erro:
        print(f"Erro ao cadastrar tarefa: {erro}")

    finally:
        conexao.close()

def listar_tarefas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT tarefas.id, tarefas.titulo, materias.nome, tarefas.status, tarefas.prioridade
    FROM tarefas
    JOIN materias ON tarefas.materia_id = materias.id
    """)
    tarefas = cursor.fetchall()

    conexao.close()
    return tarefas

def atualizar_status_tarefa(tarefa_id, novo_status):
    if not status_valido(novo_status):
        print("status inválido")
        return
    
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE tarefas
    SET status = ?
    WHERE id = ?
    """, (novo_status, tarefa_id))

    conexao.commit()
    conexao.close()

    print(
        "Status da tarefa atualizado com sucesso."
        )

def deletar_tarefa(tarefa_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM tarefas WHERE id = ?", (tarefa_id,))

    conexao.commit()
    conexao.close()

    print("Tarefa deletada com sucesso.")
    