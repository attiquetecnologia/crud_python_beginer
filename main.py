# Arquivo principal
from db import create_database
from funcoes import find_all, create, update, delete
def main():
    while True:
        print("""Menu
    1 - Mostrar tarefas
    2 - Adicionar Tarefa
    3 - Concluir Tarefa
    4 - Deletar Tarefa
    0 - Sair
    """)
        op = input("Opção do menu: ")
        if op == '1':
            for tarefa in find_all():
                print(tarefa)
        elif op == '2':
            tarefa = input("Nome da tarefa: ")
            create(tarefa)
        elif op == '3':
            for tarefa in find_all():
                print(tarefa)
            id = int(input("ID da tarefa: "))
            print(f'Concluindo tarefa {id}')
            update(id)
            
        elif op == '4':
            for tarefa in find_all():
                print(tarefa)
            id = int(input("ID da tarefa: "))
            print(f'Concluindo tarefa {id}')
            delete(id)
        elif op == '0':
            print("Saindo...")
            break
        else:
            print("Digite uma opção válida do menu")

if __name__=="__main__":
    create_database()
    #inicializa o programa
    main()