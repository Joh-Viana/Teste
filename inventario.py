inventario = {}
while True:
    print('Selecione uma opção: ')
    print('1- Adicionar itens')
    print('2- Remover itens')
    print('3- Acessar inventário')
    print('4- Sair')
    print('')
    menu = int(input())

    if menu == 1:
        while True:
            item = input('Qual item você deseja adicionar: ')
            if item in inventario:
                quantidade = int(input('Quantidade do item: '))
                inventario[item] = inventario[item] + quantidade
            else:
                quantidade = input('Quantidade do item: ')
                inventario[item] = quantidade
            
            print('')
            print('Selecione uma opção: ')
            print('1- Voltar')
            print('')

            menu_novo_item = int(input())
            if menu_novo_item == 1:
                break
    elif menu == 2:
        while True:
            item_atualizado = input('Qual item você deseja remover: ')
            if item_atualizado in inventario:
                numero_atualizado = input('Quantidade')
                agenda[nome_atualizado] = nome_atualizado
                
            else:
                print('Contato não existe')
            
            print('')
            print('Selecione uma opção: ')
            print('1- Voltar')
            print('')

            menu_atualizar_contato = int(input())
            if menu_atualizar_contato == 1:
                break       

    elif menu == 3:
        while True:
            print(inventario)

            print('')    
            print('Selecione uma opção: ')
            print('1- Voltar')
            print('')

            menu_consultar_inventario = int(input())
            if menu_consultar_inventario == 1:
                break    
    elif menu == 4:
        break