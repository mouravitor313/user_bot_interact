'''O que falta fazer:
utilizar função de lista nas opções de escolha
colocar funções de def e return
editar as ultimas partes
'''

# variáveis para a função while: 

menu0 = '0' # menu principal

menu1 = '0' # primeiro submenu

menu2 = '0' # segundo submenu 

menu3 = '0' # terceiro submenu

#variaveis do primeiro submenu para a navegação dos whiles 
horario = '0' 
clinico = '0'
pediatra = '0'
derma = '0'


checkin = '0'
preventivo = '0'
infoex = '0'
horarioex = '0'


pi = '0'
pf = '0'
cancel = '0'



# while principal: 
while (menu0 != '4'): # input pra selecionar as opções ou voltar

    print('######################') 

    print('####***  Menu  ***####') 

    print('#** Plano de saúde **#') 

    print('######################') 

    print('Opções de atendimento: ') 

    print('') 

    print('1. Marcar consulta') # sub menu 1

    print('2. Marcar exame') # sub menu 2

    print('3. Ofertas de planos e outros assuntos') # sub menu 3

    print('4. Sair') # fechar o codigo

    menu0 = input('') # input para selecionar as opções ou sair do codigo

    print('') 

    # opção 1 "Marcar consulta."
    if menu0 == '1': # se o menu for igual a alternativa 1:
        while (menu1 != '4'): # enquanto o menu 1 for diferente de 4:

            print('**Marcar consulta**')
            print('')
            print('1. Clinico Geral')
            print('2. Pediatra')
            print('3. Dermatologista')
            print('4. Voltar') 

            menu1 = input('') # input pra selecionar as opções ou voltar

            print('') 
            if menu1 == '1': # se o menu1 (primeiro sub menu) for igual a opção 1:

                while (clinico != '4'): # enquanto o menu 1 for diferente de 4:
                    print('**Clinico Geral**')
                    print('Médicos disponíveis:')
                    print('')
                    print('1. Dr. Silva')
                    print('2. Dr. Cunha')
                    print('3. Dr. Nascimento')
                    print('4. Voltar')
                    print('')

                    clinico = input('') # input para escolher o medico.

                    if clinico == '1': # se o medico escolhido for igual a opção 1
                        print ('')
                        print ('Dr. Silva.') # printa o médico escolhido
                        print ('')
                    elif clinico == '2': # se o medico escolhido for igual a opção 2
                        print ('')
                        print ('Dr. Cunha.') # printa o medico escolhido
                        print('')
                    elif clinico == '3': # se o medico escolhido for igual a opção 3
                        print('')
                        print ('Dr. Nascimento.') # printa o medico escolhido
                        print('')
                    elif clinico == '4': # se for escolhida a opção de voltar ele vai voltar
                        print ('') # e printar um espaço
                    else: # se não:
                        print ('Escolha inválida!') # caso for digitado uma opção inválida
                    print ('')
                    while (horario != '4'): # enquanto o horario for diferente de 4:
                        print ('Escolha um horário:')
                        print('')
                        print ('1. Dia')
                        print ('2. Tarde')
                        print ('3. Noite') 
                        print ('4. Voltar')
                        print ('')

                        horario = input('') # entrada de teclado para escolher uma das opções
                        if horario == '1': # se o horario for igual a 1:
                            print ('Dia') # printa a hora do periodo do horario 1
                        elif horario == '2': # se o horario for igual a 2:
                            print ('Tarde') # printa a hora do periodo do horario 2
                        elif horario == '3': # se o horario for igual a 3:
                            print ('Noite')# printa a hora do periodo do horario 3
                        elif horario == '4': # se o horario for igual a 4:
                            print ('') # printa um espaço e volta pro loop while anterior
                        else: # se não
                            print ('Escolha inválida!') # printa que a escolha é invalida e recomeça o while do horario
                        print('')
                        if clinico == '1' and horario == '1': # se o clinico for igual a 1 e o horario for igual a 1
                            print('Consulta marcada às 08:30h com o Dr. Silva.') # printa o resultado das escolhas
                            print('')
                            break
                        if clinico == '1' and horario == '2': # se o clinico for igual a 1 e o horario igual a 2
                            print('Consulta marcada às 14:00h com o Dr. Silva.') # printa o resultado das escolhas
                            print('')
                            break
                        if clinico == '1' and horario == '3': # se o clinico for igual a 1 e o horario igual a 3
                            print('Consulta marcada às 19:30h com o Dr. Silva.') # printa o resultado das escolhas
                            print('')
                            break
                        if clinico == '2' and horario == '1': # se o clinico for igual a 2 e o horario igual a 1
                            print('Consulta marcada às 09:00h com o Dr. Cunha') # printa o resultado das escolhas
                            print('')
                            break
                        if clinico == '2' and horario == '2': # se o clinico for igual a 2 e o horario igual a 2
                            print('Consulta marcada às 15:30h com o Dr. Cunha') # printa o resultado das escolhas
                            print('')
                            break
                        if clinico == '2' and horario == '3': # se o clinico for igual a 2 e o horario igual a 3
                            print('Consulta marcada às 18:45h com o Dr. Cunha') # printa o resultado das escolhas
                            print ('')
                            break 
                        if clinico == '3' and horario == '1': # se o clinico for igual a 3 e o horario igual a 1
                            print('Consulta marcada às 09:00h com o Dr. Nascimento') # printa o resultado das escolhas
                            print('')
                            break
                        if clinico == '3' and horario == '2': # se o clinico for igual a 3 e o horario igual a 2
                            print('Consulta marcada às 15:30h com o Dr. Nascimento') # printa o resultado das escolhas
                            print('')
                            break
                        if clinico == '3' and horario == '3': # se o clinico for igual a 3 e o horario igual a 3
                            print('Consulta marcada às 18:45h com o Dr. Nascimenti') # printa o resultado das escolhas
                            print ('')
                            break
                    break
                break 
            if menu1 == '2':
                while (pediatra != '4'):
                    print('**Pediatra**')
                    print('Médicos disponíveis:')
                    print('')
                    print('1. Dr. Pereira')
                    print('2. Dr. Lima')
                    print('3. Dr. Almeida')
                    print('4. Sair')
                    print('')
                    pediatra = input('')

                    if pediatra == '1':
                        print ('')
                        print ('Dr. Pereira.')
                        print ('')
                    elif pediatra == '2':
                        print ('')
                        print ('Dr. Lima.')
                        print('')
                    elif pediatra == '3':
                        print('')
                        print ('Dr. Almeida.')
                        print('')
                    elif pediatra == '4':
                        print ('')
                    else:
                        print ('Escolha inválida!')
                    print ('')
                    while (horario != '4'):
                        print ('Escolha um horário:')
                        print('')
                        print ('1. Dia')
                        print ('2. Tarde')
                        print ('3. Noite') 
                        print ('4. Voltar')

                        print ('')
                        horario = input('')
                        print ('')
                        if horario == '1':
                            print ('Dia')
                        elif horario == '2':
                            print ('Tarde')
                        elif horario == '3':
                            print ('Noite')
                        elif horario == '4':
                            print ('')
                        else:
                            print ('Escolha inválida!')
                        print('')
                    
                        if pediatra == '1' and horario == '1':
                            print('Consulta marcada às 08:30h com o Dr. Pereira.')
                            print('')
                            break
                        if pediatra == '1' and horario == '2':
                            print('Consulta marcada às 14:00h com o Dr. Pereira.')
                            print('')
                            break
                        if pediatra == '1' and horario == '3':
                            print('Consulta marcada às 19:30h com o Dr. Pereira.')
                            print('')
                            break 
                        if pediatra == '2' and horario == '1':
                            print('Consulta marcada às 09:00h com o Dr. Lima')
                            print('')
                            break
                        if pediatra == '2' and horario == '2':
                            print('Consulta marcada às 15:30h com o Dr. Lima')
                            print('')
                            break
                        if pediatra == '2' and horario == '3':
                            print('Consulta marcada às 18:45h com o Dr. Lima')
                            print ('')
                            break 
                        if pediatra == '3' and horario == '1':
                            print('Consulta marcada às 09:00h com o Dr. Almeida')
                            print('')
                            break
                        if pediatra == '3' and horario == '2':
                            print('Consulta marcada às 15:30h com o Dr. Almeida')
                            print('')
                            break
                        if pediatra == '3' and horario == '3':
                            print('Consulta marcada às 18:45h com o Dr. Almeida')
                            print ('')
                            break
                    break
            if menu1 == '3':
                while (derma != '4'):
                    print('**Dermatologista**')
                    print('Médicos disponíveis:')
                    print('')
                    print('1. Dr. Costa')
                    print('2. Dr. Tenma')
                    print('3. Dr. Santos')
                    print('4. Sair')
                    print('')
                    derma = input('')
                    if derma == '1':
                        print ('')
                        print ('Dr. Costa.')
                        print ('')
                    elif derma == '2':
                        print ('')
                        print ('Dr. Tenma.')
                        print('')
                    elif derma == '3':
                        print('')
                        print ('Dr. Santos.')
                        print('')
                    elif derma == '4':
                        print ('')
                    else:
                        print ('Escolha inválida!')
                    print ('')
                    while (horario != '4'):
                        print ('Escolha um horário:')
                        print('')
                        print ('1. Dia')
                        print ('2. Tarde')
                        print ('3. Noite') 
                        print ('4. Voltar')

                        print ('')
                        horario = input('')
                        print ('')
                        if horario == '1':
                            print ('Dia')
                        elif horario == '2':
                            print ('Tarde')
                        elif horario == '3':
                            print ('Noite')
                        elif horario == '4':
                            print ('')
                        else:
                            print ('Escolha inválida!')
                        print('')
                        if derma == '1' and horario == '1':
                            print('Consulta marcada às 08:30h com o Dr. Costa.')
                            print('')
                            break
                        if derma == '1' and horario == '2':
                            print('Consulta marcada às 14:00h com o Dr. Costa.')
                            print('')
                            break
                        if derma == '1' and horario == '3':
                            print('Consulta marcada às 19:30h com o Dr. Costa.')
                            print('')
                            break 
                        if derma == '2' and horario == '1':
                            print('Consulta marcada às 09:00h com o Dr. Tenma')
                            print('')
                            break
                        if derma == '2' and horario == '2':
                            print('Consulta marcada às 15:30h com o Dr. Tenma')
                            print('')
                            break
                        if derma == '2' and horario == '3':
                            print('Consulta marcada às 18:45h com o Dr. Tenma')
                            print ('')
                            break 
                        if derma == '3' and horario == '1':
                            print('Consulta marcada às 09:00h com o Dr. Santos')
                            print('')
                            break
                        if derma == '3' and horario == '2':
                            print('Consulta marcada às 15:30h com o Dr. Santos')
                            print('')
                            break
                        if derma == '3' and horario == '3':
                            print('Consulta marcada às 18:45h com o Dr. Santos')
                            print ('')
                            break
                    break
                break

    if menu0 == '2': 
        while (menu2 != '4'): 

            print('º**Marcar exames**º') 
            
            print('1. Check-in') 

            print('2. Preventivo') 

            print('3. Informações') 

            print('4. Voltar') 
            
            print('')
            
            menu2 = input('') 

            print('') 

        if menu2 == '1': 
            while (checkin != '2'):
                print ('Check-in')
                print ('1. Marcar exame.')
                print ('2. Voltar')
                print ('')
                if checkin == '1':
                    while (horarioex != '3'):
                        print('Escolha um horario:')
                        print('1. Dia')
                        print('2. Tarde')
                        print('3. Voltar')
                        print('')
                        horarioex = input('')
                        if horarioex == '1':
                            print ('Exame marcado na unidade de Nova Iguaçu. Compareca entre os horários de 8:30h ás 10:00h.')
                            print ('Compareça em jejum de 12h.')
                            break
                        elif horarioex == '2':
                            print ('Exame marcado na unidade de Nova Iguaçu. Compareca entre os horários de 13:00h ás 15:30h.')
                            print ('Compareça em jejum de 12h.')
                            break
                        elif horarioex == '3':
                            print('')
                        else: 
                            print('Opção inválida!')
                    break
                break

        elif menu2 == '2': 
            while (preventivo != '2'):
                print ('Preventivo')
                print ('1. Marcar exame.')
                print ('2. Voltar')
                print ('')
                if preventivo == '1':
                    while (horarioex != '3'):
                        print('Escolha um horario:')
                        print('1. Dia')
                        print('2. Tarde')
                        print('3. Voltar')
                        print('')
                        horarioex = input('')
                        if horarioex == '1':
                            print ('Exame marcado na unidade de Nova Iguaçu. Compareca entre os horários de 8:30h ás 10:00h.')
                            print ('Compareça em jejum de 12h.')
                            break
                        elif horarioex == '2':
                            print ('Exame marcado na unidade de Nova Iguaçu. Compareca entre os horários de 13:00h ás 15:30h.')
                            print ('Compareça em jejum de 12h.')
                            break
                        elif horarioex == '3':
                            print('')
                        else: 
                            print('Opção inválida!') 
                    break
                break
                                    
        elif menu2 == '3': 
            while (infoex != '3'):
                print ('Informações')
                print ('1. Informações sobre o Check-in')
                print ('2. Informações sobre o preventivo')
                print ('3. Voltar')
                print ('')
                if infoex == '1':
                    print('Informações sobre o Check-in:')
                    print('')
                    print('O exame de check-in serve para encontrar problemas através de uma pequena bateria de exames.')
                    print('O check-in do plano cobre: ')
                    print('Hemograma completo, Glicemia, Colesterol e triglicerideos, ureia e creatina.')
                    print('Exame de urina')
                    print('')
                    break
                if infoex == '2':
                    print('Informações sobre o Preventivo:')
                    print('')
                    print('O exame preventivo, também conhecido como exame de Papanicolau, é um exame ginecológico indicado para mulheres sexualmente ativas e que tem como objetivo avaliar o colo do útero, verificando se há sinais que indiquem infecção pelo HPV')
                    print('')
                    break
            break
        
        elif menu2 == '4':    
            print ('')

        else:
            print('Escolha inválida!')
        print ('')
    if menu0 == '3': 

        while (menu3 != '4'): 

            print('Oferta de planos e outros assuntos:') 
            
            print('1. Planos individuais') 

            print('2. Planos familiares') 

            print('3. Cancelamento ou mudança de planos') 

            print('4. Voltar') 
            
            print('')
            
            menu3 = input('') 

            print('') 
        if menu3 == '1':
            while (pi != '3'): 
                print ('**Planos individuais**') 
                print ('') 
                print('1. Planos basicos')
                print('2. Planos avançados')
                print('3. Voltar')
                pi = input ('')
                if pi == '1': 
                    print ('Fale com um de nossos corretores sobre planos de saúde básicos:') 
                    print ('21 9xxxx-xxxx') 
                    print ('') 

                elif pi == '2': 
                    print ('Fale com um de nossos corretores sobre planos de saúde avançados:') 
                    print ('21 9xxxx-xxxx')
                    print ('') 

                elif pi == '3':    
                    print ('')

                else:
                    ('Escolha inválida!')
        if menu3 == '2':
            while (pf != '3'):
                print ('')
                print ('**Planos familiares**') 
                print ('') 
                print('1. Planos basicos')
                print('2. Planos avançados')
                print('3. Voltar')
                pf = input ('')
                if pf == '1': 
                    print ('Fale com um de nossos corretores sobre planos de saúde básicos:') 
                    print ('21 9xxxx-xxxx') 
                    print ('') 

                elif pf == '2': 
                    print ('Fale com um de nossos corretores sobre planos de saúde avançados:') 
                    print ('21 9xxxx-xxxx')
                    print ('') 

                elif pf == '3':    
                    print ('')

                else:
                    ('Escolha inválida!')
        if menu3 == '3':
            while (cancel != '3'): 
                print ('**Cancelamento ou mudança de planos**') 
                print ('') 
                print('1. Mudança de planos')
                print('2. Cancelamento')
                print('3. Voltar')
                if cancel == '1': 
                    print ('Fale com um de nossos atendentes para poder efetuar uma mudança de planos:') 
                    print ('21 9xxxx-xxxx') 
                    print ('') 

                elif cancel == '2': 
                    print ('Fale com um de nossos atendentes para poder efetuar um cancelamento do seu plano:') 
                    print ('21 9xxxx-xxxx')
                    print ('') 

                elif cancel == '3':    
                    print ('')

                else:
                    ('Escolha inválida!')

        print ('')


        print ('')


        
    if menu0 == '4': 

        print('Obrigado.')