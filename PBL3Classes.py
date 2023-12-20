from PBL3Funções import criarlinha

# Classe criada para padronizar o cadastro dos pacientes da clinica
class Paciente:
    'Classe que cria um objeto paciente.'

    # Metodo construtor e seus parametros de cadastro, recebe nome CPF e um id como parâmetros
    def __init__(self, nome, CPF, id:int):
        
        self.nome = nome
        self.CPF = CPF
        self.id = id

# Classe criada para padronizar e organizar o cadastro das Sessões de atendimento da clinica
class Sessão:
    'Classe que cria um objeto Sessão'

    # Metodo construtor e seus parametros de cadastro, recebe Data, Horario e tempo da sessão como parâmetros
    def __init__(self, Data, Horario, tempoSessao, id:int):

        self.Data = Data
        self.Horario = Horario
        self.tempoSessao = tempoSessao
        self.id = id

# Classe criada para definir os metodos e ações da recepção e do dentista da clínica
class Clinica:
    'Classe que contém as ações da Recepção e do Dentista'

    # Lista que armazenam objetos Sessão
    sessoes = []
    # Lista que armazenam objetos Pacientes
    pacientes = []
    # Lista de pacientes que estão na fila de atendimento
    fila = []
    # Dicionarios utilizados para armazenar as informações dos objetos Sessão e Paciente e acessa-los com mais facilidade
    cadastroSessoes= {}
    cadastroPacientes = {}
    # lista e dicionarios que armazena sessões e pacientes que se relacionam
    sessaoPaciente = []
    dicionarioSessaoPaciente = {}
    # Lista que faz referência as consultas realizadas a sessão do dia
    consultasSessao = []

    # Inicio dos métodos da clínica

    # Metodo que adiciona o objeto Sessão criado no sistema
    def adicionarSessao(self, object):
        self.cadastroSessoes['Data'] = object.Data
        self.cadastroSessoes['Horario'] = object.Horario
        self.cadastroSessoes['Tempo da Sessao'] = object.tempoSessao
        self.cadastroSessoes['id'] = object.id
        self.sessoes.append(self.cadastroSessoes.copy())

        # adicionando o id da sessao em um dicionario para ser utilizado como ferramenta de busca e confirmação de sessoes

        self.dicionarioSessaoPaciente['sessaoID'] = object.id
        self.dicionarioSessaoPaciente['pacientesID'] = []
        self.sessaoPaciente.append(self.dicionarioSessaoPaciente.copy())

        print('Sessão criada com sucesso.')
    
    # Método que lista as sessões já adicionadas no sistema
    def listarSessoes(self):
        for i in self.sessoes:
            print(i, end= '')
            print()
    
    # Método que busca e retorna sessões cadastradas com base na data e horario
    def buscarSessao(self):
        Data = input('Digite a data da sessão [dd/mm/aaaa]: ')
        Horario = input('Digite o horario de inicio da sessão [hh:mm]: ')
        
        # Loop percorre a lista "sessoes" e compara os valores das variaveis com as chaves dos dicionarios
        for s in self.sessoes:
            if s['Data'] == Data and s['Horario'] == Horario:
                return s

    # Método que inicia e retorna a sessão do dia caso ela exista no sistema
    def iniciarSessao(self):
        iniciar = self.buscarSessao()

        if iniciar != None:
            print('Sessão iniciada.')

            return iniciar['id']
    
    def encerrarSessao(self, sessaoAtiva):
        if sessaoAtiva != None or sessaoAtiva != 0:
            encerrarSessao = 0
            print('Sessão encerrada.')
            for s in self.sessoes:
                if s['id'] == sessaoAtiva:
                    self.sessoes.remove(s)

            return encerrarSessao

    # Método que adiciona objetos pacientes no sistema
    def adicionarPaciente(self, object):
        self.cadastroPacientes['nome'] = object.nome
        self.cadastroPacientes['CPF'] = object.CPF
        self.cadastroPacientes['id'] = object.id
        self.cadastroPacientes['prontuarios'] = []
        self.pacientes.append(self.cadastroPacientes.copy())
        print('Paciente cadastrado com sucesso.')

    # Método que adiciona aos objetos pacientes cadastrados as sessões de consulta que eles marcaram, passando Data, Horario e CPF
    def marcarHorario(self, CPF):
        sessao = self.buscarSessao()
        # verifica se a sessão buscada se encontra do sistema
        if sessao != None:
            '''Loop percorre lista de pacientes e adiciona a variavel "paciente" e a lista "confirmaçãoPaciente" caso o paciente seja 
            encontrado'''
            confirmaçãoPaciente = []
            for p in self.pacientes:
                if p['CPF'] == CPF:
                    # Adicionando id do paciente encontrado na variavel paciente
                    paciente = p['id']
                    confirmaçãoPaciente.append(paciente)
            
            # verifica se o paciente está cadastrado no sistema
            if len(confirmaçãoPaciente) > 0:
                # loop percorre a lista "sessaoPaciente" e faz a Linkagem entre id paciente e id sessão 
                for s in self.sessaoPaciente:
                    if s['sessaoID'] == sessao['id']:
                        # verifica se o paciente já está cadastrado na sessão
                        if paciente in s['pacientesID']:
                            print('Paciente já cadastrado nessa sessão')
                        else:
                            s['pacientesID'].append(paciente)
                            print('Horário marcado.')
            
            else:
                print('Paciente não Cadastrado no sistema.')

        else:
            print('Sessão não encontrada.')

    # Método que lista os pacientes cadatrados no sistema
    def listarPacientes(self):
        for p in self.pacientes:
            print(f'|{p}|', end='')
            print()
    
    # Método que lista os horários de um pacientes cadastrado no sistema com base no seu ID
    def horarioPacientes(self, CPF):
        sessoesDoPaciente = []
        # loop percorre a lista "pacientes" e verificva se o CPF informado está na lista
        for p in self.pacientes:
            if p['CPF'] == CPF:
                # loop percorre a lista "sessaoPaciente" e verifica se o ID do paciente informado está na lista
                for x in self.sessaoPaciente:
                    if p['id'] in x['pacientesID']:
                        # loop percorre a lista "sessões" e adiciona na lista "sessoesDoPaciente" a sessão que o paciente se encontra
                        for s in self.sessoes:
                            if x['sessaoID'] == s['id']:
                                sessoesDoPaciente.append(s)
        
        # condicional verifica se o paciente informado possui ou não horários marcados
        if sessoesDoPaciente:
            print('Horários do paciente')
            print()
            for i in sessoesDoPaciente:
                print(i)
                criarlinha()

        else:
            print('O paciente não tem horários marcados ou não está cadastrado no sistema.')

    # Método que confirma se um paciente tem horário marcado na sessão iniciada e o adiciona na fila de atendimento
    def confirmarHorario(self, sessaoAtiva, CPF):
        # verifica se sessaoAtiva possui valor não nulo ou igual a 0
        if sessaoAtiva != None and sessaoAtiva != 0:
            # loop percorre a lista "sessaoPaciente" e seus dicionario e a variavel sessaoID recebe o id da sessao
            for i in self.sessaoPaciente:
                for s in i.values():
                    if sessaoAtiva == s:
                        sessaoID = s
            
            # loop percorre a lista "sessaoPaciente" e a variavel "pacienteID" recebe o id do paciente informado 
            for x in self.sessaoPaciente:
                if x['sessaoID'] == sessaoID:
                    pacienteID = x['pacientesID']

            # loop percorre lista "pacientes" e verifica se o paciente informado se encontra
            for p in self.pacientes:
                if p['CPF'] == CPF:
                    if sessaoAtiva != 0:
                        if p['id'] in pacienteID:
                            print('O paciente está presente na sessão e será adicionado na fila automaticamente.')

                            self.fila.append(p['nome'])
                            print('Paciente adicionado na fila')
                        
                        else:
                            print('O paciente não se encontra nessa sessão.')
        
        else:
                    print('A sessão não foi iniciada.')

    # Método que lista o primeiro paciente a ser atendido com base na fila de atendimento
    def listarPrimeiroDaFila(self):
        if len(self.fila) > 0:
            print(f'O próximo paciente da fila é: {self.fila[0]}')

        else:
            print('Fila vazia.')
            
    # Método que lista as consultas realizadas na clínica 
    def listarConsultas(self):
        if len(self.consultasSessao) > 0:
            print('-='*30)
            print('Lista de consultas')

            for c in self.consultasSessao:
                print(c, end='')
                print()

            criarlinha()
        
        else:
            print('Nenhuma consulta realizada.')

    # Inicio dos métodos do dentista

    # Método que localiza a sessão pra o dentista a partir da data e do horário
    def localizarSessão(self):
        sessao = self.buscarSessao()
        if sessao != None:
            print('Sessão clínica encontrada.')
            print(sessao)
        
        else:
            print('Sessão clínica não encontrada.')
    
    # Método que permite o dentista atender um paciente, retirando este da fila 
    def atenderPaciente(self):

        # verifica se a lista possui algum paciente pronto para atendimento e o encaminha para a sala de consulta
        if len(self.fila) > 0:
            paciente = self.fila.pop(0)
            print(f'Paciente {paciente} encaminhado para o antendimento.')
            print('Retirando paciente da fila de antedimento.')
            
            return paciente

        else: 
            print('Não foi possivel encaminhar o paciente pois a fila está vazia.')

    # Método que permite o dentista adicionar ao paciente seu protuario de sessão
    def anotarProntuario(self, nome):
        if nome != None:
            # após a verificação da variavel "nome" o loop percorre a lista "Pacientes" possibilitando a anotação do prontuario 
            for p in self.pacientes:
                if p['nome'] == nome:
                    prontuario = input('Digite o prontuário do paciente: ')
                    data = input('Digite a data do atendimento: [dd/mm]')
                    anotação = (prontuario, data, nome)
                    # sistema salva o prontuário do paciente em seu cadastro 
                    p['prontuarios'].append(anotação)
                    print('Prontuário anotado.')
                    # lista consultasSessao recebe o prontuário, a data da consulta e o nome do paciente
                    self.consultasSessao.append((nome,anotação))
        
        else:
            print('Não é possível anotar prontuários, nenhum paciente foi atendido.')
    
    # Método que permite a visualização do primeiro prontuário de um paciente 
    def primeiroProntuario(self, nome):
        if nome != None:
            '''após a verificação da variavel "nome" o loop percorre a lista "Pacientes" possibilitando a leitura do primeiro prontuario
            do paciente'''
            for p in self.pacientes:
                if p['nome'] == nome:
                    print(f'O primeiro prontuário de {p['nome']} foi: {p['prontuarios'][0]}')
        
        else:
            print('Não é possivel ler o primeiro prontuário nesse momento.')
    
    # Método que permite a visualização do ultimo prontuário de um paciente 
    def ultimoProntuario(self, nome):
        if nome != None:
            '''após a verificação da variavel "nome" o loop percorre a lista "Pacientes" possibilitando a leitura do ultimo prontuario
            do paciente'''
            for p in self.pacientes:
                if p['nome'] == nome:
                    print(f'O último prontuário de {p['nome']} foi: {p['prontuarios'][-1]}')
        
        else:
            print('Não é possível ler o último prontuário nesse momento.')