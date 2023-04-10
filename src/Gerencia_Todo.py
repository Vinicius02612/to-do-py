from To_do import ToDo
import emoji

list_todo  = []

def create_todo():
    id = input('informe o id: ')
    titulo =  input('informe o titulo da task: ')
    descricao =  input('informe a descrição:')
    status = False

    task = ToDo(id, titulo, descricao, status)

    for i in list_todo:
        if i.id and i.titulo:
            return False,'Tarefa ja cadastrada.'
    
    list_todo.append(task)
    return True,'Tarefa cadastrada com sucesso!'
    
def listing_all():
    if len(list_todo) == 0:
        print('Lista esta vazia \n Adicione uma tarefa.')
        create_todo()
    else:
        print('Suas tarefas\n')
        for i in list_todo:
            if i.status == True:
                print(f'id:{i.id}\n Titulo:{i.titulo}\nDescrição:{i.descricao}\n Status: Não Concluida.')
            else:
                print(f'id:{i.id}\n Titulo:{i.titulo}\nDescrição{i.descricao}\n Status: Concluida.')



    

def main():
    print(f'Bem Vindo ao app TO_DO!')
    opc = 0
    while opc >= 0:

        print('1 - Criar uma TO-DO\n2 - Listar as TO-DO\n3 - Editar uma TO-DO\n4 - Marcar TO-DO com concluida\n5 - Excluir uma TO-DO\n6 - Sair')
        opc = input('Informe  a opção desejada:')
        opc = int(opc)
        if opc == 1:
           create_todo()
        if opc == 2:
            listing_all()

    
    

if __name__ == "__main__":
    main()








        