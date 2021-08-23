#Para facilitar a indentificação de um paciente, fazemos fichas, com diversos dados, assim facilitamos a próxima
# avaliação, criarei um programa onde a criação destas ficahas sejam sempre padrões e de fácil acesso:
import datetime
#class = classe (nome da classe 'Paciente')
class Paciente:
    #def = método
    #set = atribuir
    #get = pegar

    #Nome
    def setNome(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome

    #Telefone
    def setNumero(self, numero):
        self._numero = numero

    def getNumero(self):
        return self._numero

    #Data de Nascimento
    def setAno(self, ano):
        self._ano = ano

    def getIdade(self):
        return (datetime.date.today().year - self._ano)

def dar_entrada():
    total = 1
    while total != 0:
        total -= 1
        entrada = 'a'
        while entrada != 'S' and entrada != 'N':
            ocorrencia = input('Começar/Verificar cadastro? S/N ').upper()
            if ocorrencia == 'S' or ocorrencia == 'SIM':
                ocorrencia = 'S'
                entrada = ocorrencia
            else:
                print('Quando quiser comerçar diga Sim')

def dados_diferenciais():
    #Fixa Paciente

    paciente = Paciente()
    nome = input('Nome completo: ')
    numero = input('Número para contato: ')
    ano = int(input('Ano de nascimento: '))


    paciente.setNome(nome)
    paciente.setNumero(numero)
    paciente.setAno(ano)


    print(f'Nome: {paciente.getNome()}')
    print(f'Telefone: {paciente.getNumero()}')
    print(f'O paciente tem {paciente.getIdade()} anos, até o final do ano')





def chamar_funcoes():
    #dar_entrada()
    dados_diferenciais()



chamar_funcoes()


#Diferenciação
#Nome - Telefone (Se for igual sabemos que é a mesma pessoa, logo baixamos a fixa dela.)

#Nome - Telefone (Caso não sejam iguais, buscamos mais informações, pois a pessoa pode ter mudado de n°, ou ser outra
# pessoa de mesmo nome.)

#Nome - Telefone - Data de Nascimento (Assim aumentamos a precisão, de indentificar se é ou não a mesma pessoa, caso
# a data de nascimento seja a mesma as chances de ser a mesma pessoa sobe muito.)
# As chances desses dados (nome/data) serem iguais são infímas, mas existentes

#Nome - Telefone - Data de Nascimento - Cidade Natal (Pois assim é 99,9% de chance de indentificar se é ou não a mesma
#pessoa, caso for a mesma pessoa atualizamos os dados, caso for outra pessoa crimos uma nova fixa com esses dados)