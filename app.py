from database import criar_tabelas
from services import (
    cadastrar_materia,
    listar_materias,
    cadastrar_tarefa,
    listar_tarefas,
    atualizar_status_tarefa,
    deletar_tarefa
)

def mostrar_menu():
    print("\n===== Gerenciador de Estudos =====")
    print("1. - Cadastrar matéria")
    print("2. - Listar matérias")
    print("3. - Cadastrar tarefa")
    print("4. - Listar tarefas")
    print("5. - Atualizar status da tarefa")
    print("6. - Deletar tarefa")
    print("0. - Sair")

def main():
    criar_tabelas()
    
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                nome = input("Nome da matéria; ")
                cadastrar_materia(nome)

            case "2":
                materias = listar_materias()
                if not materias:
                    print("Nenhuma matéria cadastrada")

                else:
                    for materia in materias:
                        print(f"{materia[0]} - {materia[1]}")

            case "3":
                titulo = input("Título da tarefa: ")

                materias = listar_materias()

                if not materias:
                    print("Cadastre uma matéria antes.")
                    continue

                for materia in materias:
                    print(f"{materia[0]} - {materia[1]}")

                materia_id = int(input("ID da matéria: "))
                prioridade = input("Prioridade baixa/media/alta: ").lower()

                cadastrar_tarefa(titulo, materia_id, prioridade)

            case "4":
                tarefas = listar_tarefas()

                if not tarefas:
                    print("Nenhuma tarefa cadastrada.")
                else:
                    for tarefa in tarefas:
                        print(
                f"{tarefa[0]} - {tarefa[1]} | "
                f"Matéria: {tarefa[2]} | "
                f"Status: {tarefa[3]} | "
                f"Prioridade: {tarefa[4]}"
            )

            case "5":
                tarefa_id = int(input("ID da tarefa: "))
                novo_status = input(
                    "Novo status (pendente/fazendo/concluido): "
                    )
                
                atualizar_status_tarefa(tarefa_id, novo_status)

            case "6":
                tarefa_id = int(input("ID da tarefa: "))
                deletar_tarefa(tarefa_id)

            case "0":
                print("Saindo...")
                break

            case _:
                print("Opção inválida. Tente novamente.")   

main()