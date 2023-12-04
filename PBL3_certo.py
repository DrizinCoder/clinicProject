# Classe criada para padronizar o cadastro dos pacientes da clinica
class Paciente:
    'Classe que cria um objeto paciente.'

    # Metodo construtor e seus parametros de cadastro
    def __init__(self, nome, CPF, id:int):
        
        self.nome = nome
        self.CPF = CPF
        self.id = id

    # Método que transforma as informações da classe em Str
    def toString(self):
        return f'{self.nome} {self.CPF} {self.id}'

# Classe criada para padronizar e organizar o cadastro das Sessões de atendimento da clinica
class Sessão:
    'Classe que cria um objeto Sessão'

    # Metodo construtor e seus parametros de cadastro
    def __init__(self, Data, Horario, tempoSessao):

        self.Data = Data
        self.Horario = Horario
        self.tempoSessao = tempoSessao

    # Método que transforma as informações da classe em Str
    def toString(self):
        f'{self.Data}, {self.Horario}, {self.tempoSessao}'

# Classe criada para definir os metodos e ações da recepção e do dentista da clínica
class Clinica:

    # Lista que armazenam objetos referentes a sessões clinicas e pacientes da clinica
    sessoes = []
    pacientes = []
    fila = []
    cadastroSessoes= {}
    cadastroPacientes = {}
    consultasSessao = []

    # Inicio dos métodos da clínica

    def adicionarSessao(self, object):
        self.cadastroSessoes['Data'] = object.Data
        self.cadastroSessoes['Horario'] = object.Horario
        self.cadastroSessoes['tempoSessao'] = object.tempoSessao
        self.sessoes.append(self.cadastroSessoes.copy())
        print('Sessão criada com sucesso.')
    
    def listarSessoes(self):
        for i in self.sessoes:
            print(i, end= '')
            print()
    
    def buscarSessao(self, Data, Horario):
        for s in self.sessoes:
            if s['Data'] == Data and s['Horario'] == Horario:
                return s

    def iniciarSessao(self, Data, Horario):
        iniciar = False 
        if self.buscarSessao(Data, Horario) != None:
            iniciar = True
            print('Sessão iniciada.')
        
        return iniciar

    def adicionarPaciente(self, object):
        self.cadastroPacientes['nome'] = object.nome
        self.cadastroPacientes['CPF'] = object.CPF
        self.cadastroPacientes['id'] = object.id
        self.cadastroPacientes['sessões'] = []
        self.cadastroPacientes['prontuarios'] = []
        self.pacientes.append(self.cadastroPacientes.copy())
        print('Paciente cadastrado com sucesso.')

    def marcarHorario(self, Data, Horario, CPF):
        if self.buscarSessao(Data, Horario) != None:
            sessao = self.buscarSessao(Data, Horario)
            for p in self.pacientes:
                if p['CPF'] == CPF:
                    p['sessões'].append(sessao)
                    print('Paciente adicionado com sucesso')

        else:
            print('Sessão não encontrada.')

    def listarPacientes(self):
        for p in self.pacientes:
            print(f'|{p}|', end='')
            print()
    
    def horarioPacientes(self, id):
        for p in self.pacientes:
            if p['id'] == id:
                print('-'*30)
                print(p['sessões'])

    def adicionarNaFila(self, object):
        self.fila.append(object)
        print('Paciente adicionado na fila')
    
    def listarFila(self):
        print(self.fila)

    def listarConsultas(self):
        print('-='*30)
        print('Lista de consultas')

        for c in self.consultasSessao:
            print(c, end='')
            print()

        print('-='*30)

    # Inicio dos métodos do dentista

    def localizarSessão(self, Data, Horario):
        sessao = self.buscarSessao(Data, Horario)
        if sessao != None:
            print('Sessão clínica encontrada.')
            print(sessao)
        
        else:
            print('Sessão clínica não encontrada.')
    
    def atenderPaciente(self):

        if len(self.fila) > 0:
            paciente = self.fila.pop(0)
            print(f'Paciente {paciente} encaminhado para o antendimento.')
            print('Retirando paciente da fila de antedimento.')
            self.consultasSessao.append(paciente)

        else: 
            print('Não foi possivel encaminhar o paciente pois a fila está vazia.')

    
    def anotarProntuario(self, CPF):
        for p in self.pacientes:
            if p['CPF'] == CPF:
                prontuario = input('Digite o prontuário do paciente: ')
                p['prontuarios'].append(prontuario)
                print('Prontuário anotado.')
        
        while True:
            atualProntuário = input('Deseja ler o prontuário?[S/N]: ').upper()
            if atualProntuário == 'S':
                print(f'O prontuário anotado foi {prontuario}')
                break
            
            elif atualProntuário == 'N':
                break

            else:
                print('Caracter inválido. Use [S/N].')
    
    def primeiroProntuario(self, CPF):
        for p in self.pacientes:
            if p['CPF'] == CPF:
                print(f'O primeiro prontuário de {p['nome']} foi: {p['prontuarios'][0]}')
    
    def ultimoProntuário(self, CPF):
        for p in self.pacientes:
            if p['CPF'] == CPF:
                print(f'O último prontuário de {p['nome']} foi: {p['prontuarios'][-1]}')

