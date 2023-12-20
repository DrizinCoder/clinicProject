import os
from PBL3Classes import Paciente
from PBL3Classes import Sessão
from PBL3Classes import Clinica
from PBL3Funções import criarlinha

# Programa principal

sessaoAtiva = 0
pacienteID = 0
sessaoID = 0
nome = 0

c = Clinica()

while True:

    print('''
1- Recepção
2- Dentista
0- Sair
''')
    
    while True:

        try:
            seleçãoDeMenu = int(input('Escolha o menu referente ao seu cargo na clínica: '))
            if seleçãoDeMenu >= 3:
                print('Essa opção não está presente no menu.')
            else:
                break
        
        except ValueError:
            print('Opção inválida, digite novamente')

    os.system('cls')


    while seleçãoDeMenu == 1:

        criarlinha()
        print('''
1 - Cadastrar nova sessão clinica
2 - Listar sessões clinicas
3 - Buscar sessões clinicas
4 - Iniciar sessões clinicas
5 - Cadastrar novo paciente
6 - Marcar consulta      
7 - Listar horários marcado de um paciente
8 - Confirmar se paciente está na sessão e adiciona-lo a fila
9 - Listar próximo paciente da fila de atendimento
10 - Listar consultas realizadas na sessão
11 - Encerrar sessão              
0 - Sair do menu "Recepção"   
    ''')
        criarlinha()

        while True:

            try:
                escolhaMenuRecep = int(input('Escolha a operação a ser feita: '))
                break
        
            except ValueError:
                print('Opção inválida, digite novamente')
        
        os.system('Cls')
    
        if escolhaMenuRecep == 1:
            data = input('Digite a data da sessão [dd/mm/aaaa]: ')
            horario = input('Digite o horario de inicio da sessão [hh:mm]: ')
            tempoSessao = input('Digite o tempo da sessão: ')
            sessaoID += 1
            s = Sessão(data, horario, tempoSessao, sessaoID)
            c.adicionarSessao(s)           
        
        elif escolhaMenuRecep == 2:
            c.listarSessoes()
        
        elif escolhaMenuRecep == 3:
            sessaoBuscada = c.buscarSessao()

            if sessaoBuscada != None:
                print(f'A sessão encontrada: {sessaoBuscada}')

            else:
                print('Nenhuma sessão encontrada.')

        elif escolhaMenuRecep == 4:
            sessaoAtiva = c.iniciarSessao()

            if sessaoAtiva == None:
                print('A sessão não pode ser iniciada pois não esta cadastrada no sistema.')
        
        elif escolhaMenuRecep == 5:
            nome = input('Digite o nome do paciente: ')
            cpf = input('Digite o CPF do paciente: ')
            pacienteID += 1
            p = Paciente(nome, cpf, pacienteID)
            c.adicionarPaciente(p)
            
        elif escolhaMenuRecep == 6:
            cpf = input('Digite o CPF do paciente: ')
            c.marcarHorario(cpf)

        elif escolhaMenuRecep == 7:
            cpf = input('Digite o CPF do paciente: ')
            c.horarioPacientes(cpf)
        
        elif escolhaMenuRecep == 8:
            cpf = input('Digite o CPF do paciente: ')
            c.confirmarHorario(sessaoAtiva, cpf)
        
        elif escolhaMenuRecep == 9:
            c.listarPrimeiroDaFila()
        
        elif escolhaMenuRecep == 10:
            c.listarConsultas()
        
        elif escolhaMenuRecep == 11:
            if sessaoAtiva == 0:
                print('nenhuma sessão iniciada. Não é possível inicar sessão')
            
            else:
                sessaoAtiva = c.encerrarSessao(sessaoAtiva)

        elif escolhaMenuRecep == 0:
            seleçãoDeMenu = 10
        
        else:
            print('opção inválida. Digite uma opção disponível.')
    
    while seleçãoDeMenu == 2:

        criarlinha()
        print('''
1- Procurar sessão clínica registrada
2- Iniciar Sessão clínica
3- Atender paciente
4- Anotar prontuário
5- Ler primeiro prontuário de um paciente
6- Ler último prontuário de um paciente
7- encerrar sessão
0- Sair do menu "Dentista"
''')
        criarlinha()

        while True:

            try:
                escolhaMenuDentista = int(input('Escolha a operação a ser feita: '))
                break
        
            except ValueError:
                print('Opção inválida, digite novamente')
        
        os.system('Cls')
    
        if escolhaMenuDentista == 1:
            c.localizarSessão()
        
        elif escolhaMenuDentista == 2:
            sessaoAtiva = c.iniciarSessao()

            if sessaoAtiva == None:
                print('A sessão não pode ser iniciada pois não esta cadastrada no sistema.')

        # VERIFIQUE SE ALGUM PACIENTE ESTÀ SENDO ATENDIDO PARA EVITAR ERROS DE ANOTAR E LER PRONTUÁRIOS
        # ADICIONE UM MÉTODO NA FUNÇÃO CLÍNICA QUE PERMITE A LEITURA DE TODOS OS PRONTUÁRIOS DO PACIENTE 

        elif escolhaMenuDentista == 3:
            nome = c.atenderPaciente()
        
        elif escolhaMenuDentista == 4:
            if nome == 0:
                print('nenhum paciente chamado para consulta.')
            else:
                c.anotarProntuario(nome)

        elif escolhaMenuDentista == 5:
            if nome == 0:
                print('nenhum paciente chamado para consulta.')
            else:
                c.primeiroProntuario(nome)

        elif escolhaMenuDentista == 6:
            if nome == 0:
                print('nenhum paciente chamado para consulta.')
            else:
                c.ultimoProntuario(nome)
        
        elif escolhaMenuDentista == 7:
            if sessaoAtiva == 0:
                print('nenhuma sessão iniciada. Não é possível inicar sessão')
            
            else:
                sessaoAtiva = c.encerrarSessao(sessaoAtiva)
        
        elif escolhaMenuDentista == 0:
            break
        
        else:
            print('Caracter inválido. Digite um aopção válida.')
    
    if seleçãoDeMenu == 0:
        break
