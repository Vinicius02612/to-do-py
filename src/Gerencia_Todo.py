from To_do import ToDo

list_todo  = [] #lista de obetos que irá conter as tarefas



def createATodo():
    idNew = int(input('informe o id: '))
    titulo =  input('informe o titulo da task: ')
    descricao =  input('informe a descrição:')

    task = ToDo(idNew, titulo, descricao)

    for i in list_todo:
        if i.id  == idNew:
            return False,'\n Tarefa ja cadastrada.\n'
    
    list_todo.append(task)
    return True,'\n Tarefa cadastrada com sucesso!\n'
    
def listingAll():
    if len(list_todo) == 0:

        print('Lista esta vazia \n Adicione uma tarefa.')
        retornoCreate = createATodo()
        print(retornoCreate[1])

    else:

        print('Suas tarefas\n')
        for i in list_todo:
            print(f'id:{i.id}\nTitulo:{i.titulo}\nDescrição{i.descricao}\nStatus: {i.status}.\n')
            
def ToEdit():

    idSecond = int(input('informe o id da TO-DO que dejesa Editar:'))
    for i in list_todo:
        if  idSecond  == i.id:
            print('\n')
            opc =  int(input('Deseja alterar o \n1-titulo\n 2-Descrição\n3-Status\n\n 4-ALTERAR TODOS\n'))
            if opc == 1:

                novoTitulo = input('Informe o titulo: ')
                i.titulo = novoTitulo
                return True, '\nTarefa alterada com sucesso\n'
            
            if opc == 2:

                newDescricao = input('Informe a descrição: ')
                i.descricao = newDescricao
                return True, '\nTarefa alterada com sucesso\n'
            
            if opc == 3:
                opcStatus = int(input('\n1 - Concluido ou 0 -  Não concluido\n'))

                if opcStatus == 1:
                    i.status = True
                    return True, '\nTarefa alterada com sucesso\n'
                if opcStatus == 0:
                    i.status = False
                    return True, '\nTarefa alterada com sucesso\n'
                
            if opc == 4:

                nTitulo =  input('Informe o titulo: ')
                nDescricao = input('Informe a descrição: ')
                nStatus = int(input('infrome o status da tarefa\n 1 - Concluida\n 0 - Não conlcuida\n'))
                i.titulo = nTitulo
                i.descricao = nDescricao
              
                if nStatus == 1:
                    i.status = True
                if nStatus == 0:
                    i.status = False

                return True, 'Tarefa alterada com sucesso\n'
        return False, 'Não foi possivel encontrar a tarefa\n'


def removeTodo():
    Remove = int(input('informe o id da TO-DO que deseja remover:'))
    for i, x in enumerate(list_todo):
        print(x.id)
        if Remove == x.id:
            list_todo.remove(x)
    
    
    return False,'Tarefa não encontrada.'

    

def main():
    print('Bem Vindo ao app TO_DO!')
    opc = 0
    while opc >= 0:

        print('1 - Criar uma TO-DO\n2 - Listar as TO-DO\n3 - Editar uma TO-DO\n4 - Excluir uma TO-DO\n5 - Sair')
        opc = input('Informe  a opção desejada:')
        opc = int(opc)
        if opc == 1:
           retornoCreate = createATodo()
           print(retornoCreate[1])
        if opc == 2:
            listingAll()
        if opc == 3:
            retornoEdit = ToEdit()
            print(retornoEdit[1])
        if opc == 4:
            removeTodo()

    
    

if __name__ == "__main__":
    main()








        