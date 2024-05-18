agenda = {}
while True:
    print('Selecione uma opção: ')
    print('1- Adicionar um contato')
    print('2- Atualizar a contato')
    print('3- Consultar agenda')
    print('4- Sair')
    print('')
    menu = int(input())

    if menu == 1:
        while True:
            nome = input('Digite o nome do contato: ')
            if nome in agenda:
                print('Contato já cadastrado')
            else:
                numero = input('Digite o número: ')
                agenda[nome] = numero
            
            print('')
            print('Selecione uma opção: ')
            print('1- Voltar')
            print('')

            menu_novo_produto = int(input())
            if menu_novo_produto == 1:
                break
    elif menu == 2:
        while True:
            nome_atualizado = input('Qual contato deseja atualizar: ')
            if nome_atualizado in agenda:
                numero_atualizado = input('Qual o novo número: ')
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
            contato_consulta = input('Digite o nome do contato:')
            if contato_consulta in agenda:
                print('Nome: '(contato_consulta) + 'Número:' + agenda[contato_consulta])
            else:
                print('Contato não cadastrado')

            print('')    
            print('Selecione uma opção: ')
            print('1- Voltar')
            print('')

            menu_consultar_agenda = int(input())
            if menu_consultar_agenda == 1:
                break    
    elif menu == 4:
        break