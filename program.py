"""
Todas as informações utilizadas para a constução desse programa vem de fontes confiáveis, então não veja
esse programa como um programa qualquer. Se você, através dos testes contidos no programa, recebeu alguma
recomendação você pode optar por segui-las.

fontes:
https://coronavirus.ufsc.br/2021/09/21/10-medidas-de-prevencao-a-covid-19/
https://www.who.int/news-room/questions-and-answers/item/coronavirus-disease-covid-19-how-is-it-transmitted
https://www.gov.br/saude/pt-br
https://www.saude.sc.gov.br/coronavirus/arquivos/Manual_23-10-atualizado.pdf
https://coronavirus.saude.mg.gov.br/blog/157-tratamento-casos-leves-covid19
"""

covid_dic = {'pergunta1': ('Não posso compartilhar objetos pessoais, pois essa é uma das formas do'
                           ' vírus se propagar.', 'Verdadeiro'),

             'pergunta2': ('Não tem problema deixar de higienizar compras do mercado, afinal eu peguei'
                           ' por conta própria.', 'Falso'),

             'pergunta3': ('Mesmo que eu já tenha tomado a Vacina, preciso manter a distância de outras pessoas,'
                           ' pois posso contrair a nova variante do COVID-19.', 'Verdadeiro'),

             'pergunta4': ('Não preciso mais usar máscara em locais públicos, pois já tomei vácina'
                           ' para me previnir contra o vírus.', 'Falso'),

             'pergunta5': ('Não preciso me preocupar se o ambiente onde eu estou tem falta de ventilação,'
                           ' afinal já estou higienizado e usando máscara.', 'Falso'),
             }

lista_de_sintomas = ['febre', 'tosse', 'cansaço', 'não sinto o gosto', 'não sinto cheiro', 'dor de garganta',
                     'dor de cabeça']


def pprint(simbolo, xquantidade, msg):
    print(simbolo * xquantidade)
    print(msg)
    print(simbolo * xquantidade, '\n')


class CovidOrientation:
    def __init__(self, nome, idade, escolha):
        self.nome = nome
        self.idade = idade
        self.escolha = escolha
        self.pontuacao = 0
        self.sintomas_contraidos = 0

    def quiz(self):
        print(f'---- {self.nome}, {self.idade} anos.')
        msgjp = "Esse é um jogo de perguntas e respostas, você pode usar:"
        pprint('-', len(msgjp), msgjp)

        print('''
        ----- OPÇÕES -----
        [ V ] - Verdadeiro
        [ F ] - Falso
        ''')

        for keys, values in enumerate(covid_dic):
            pprint('-', len(covid_dic[values][0]), covid_dic[values][0])
            jogador_escolha = input('Verdadeiro ou Falso? ').strip()[0].upper()
            resposta = covid_dic[values][1].upper()[0]

            if resposta == jogador_escolha:     # pontuando acertos do usuario
                self.pontuacao += 1

        if self.pontuacao == 5:     # usuário acertou todas as perguntas do quiz
            msgprbs = f'Parabéns {self.nome}, você acertou todas as questões.'
            pprint('-', len(msgprbs), msgprbs)
        else:   # usuário não soube responder uma ou mais perguntas do quiz
            msgmotivo = f'{self.nome} você poderia esclarecer para gente o motivo pelo qual você não soube ' \
                     f'responder as perguntas?'
            pprint('-', len(msgmotivo), msgmotivo)

    def lidar_com_sintomas(self):
        print(f'---- {self.nome}, {self.idade} anos.')
        usuario_sintomas = []
        while True:     # Recebendo sintomas do usuário
            msgis = 'Você pode informar quantos sintomas quiser. Informe [N] para parar o programa.'
            pprint('-', len(msgis), msgis)
            sintomas = input('Informe um sintoma: ').lower().strip()
            usuario_sintomas.append(sintomas)
            if sintomas == 'n':
                break
        for value in lista_de_sintomas:     # percorrendo a lista de sintomas e comparando com o do usuario
            if value in usuario_sintomas:
                self.sintomas_contraidos += 1

        if self.sintomas_contraidos == 0:   # usuário não tem nenhum sintoma
            msgsicon = f'{self.nome} você não tem nenhum sintoma do COVID-19, você está seguro!'
            pprint('-', len(msgsicon), msgsicon)
        elif self.sintomas_contraidos == 1:     # usuário tem um sintoma
            msgsicon = f'{self.nome} você tem um sintoma do COVID-19, cuide-se.'
            pprint('-', len(msgsicon), msgsicon)
        elif self.sintomas_contraidos == 2:     # usuário tem dois sintomas
            msgsicon = f'{self.nome} você tem dois dos sintomas do COVID-19, recomendamos' \
                      f' que você fique em casa e cuide de sua saúde.'
            pprint('-', len(msgsicon), msgsicon)
        else:   # usuário tem 3 ou mais sintomas
            msgsicon = f'{self.nome} você tem 3 ou mais dos sintomas do COVID-19, recomendamos ' \
                       f'que você faça um teste para verificar se contraíu o COVID-19'
            pprint('-', len(msgsicon), msgsicon)

    def tratamento_covid(self):
        print(f'---- {self.nome}, {self.idade} anos.\n')
        print('''
        --------------------------------------------------------------------------------------------------------
                                   RECOMENDAÇÕES PARA TRATAMENTO DO COVID-19
        
        1° - Se você está com suspeitas de ter contraído o vírus, não perca tempo, procure um médico!
        
        2° - Em casos leves de COVID-19, além dos rémedios prescrevidos pelo médico, é importante também que 
             você fique de repouso e faça a ingestão de líquidos para ter uma boa recuperação.
            
            - As principais medidas a serem realizadas pelos pacientes em casos leves são:
                - controlar os sintomas para ter mais conforto;
                - seguir as recomendações médicas;
                - realizar o isolamento doméstico e o distanciamento físico de forma adequada, reduzindo 
                  a transmissão da doença para pessoas mais vulneráveis. 
                   
        3° - Caso tenha confirmado a contração do COVID-19, você e sua família devem realizar o isolamento
             social. É recomendado realizar 10 dias de isolamento, isso inclui pessoas que moram com você.
        
        4° - As medidas de prevenção da transmissão devem ser mantidas, como isolamento social e o 
             uso de máscaras.
             
        --------------------------------------------------------------------------------------------------------
        ''')


# Boas-vindas informada fora do while para que seja informada no ínicio do programa e apenas uma vez.
msgbv = f'Seja bem-vindo as orientações sobre o COVID-19'
pprint('-', len(msgbv), msgbv)

# O usuário foi informado fora do while, para que permanecesse o mesmo até o programa parar.
usuario_nome = input("informe seu nome: ").title().strip()
usuario_idade = int(input("Informe sua idade: "))

while True:
    print('''
    ---------------- OPÇÕES ----------------
    [ 1 ] - Quiz (jogo de perguntas e respostas)
    [ 2 ] - Teste dos sintomas
    [ 3 ] - Orientação para tratamentos
    [ 4 ] - Sair do programa
    ''')

    usuario_opcao = int(input("Escolha uma opção: "))

    myClass = CovidOrientation(nome=usuario_nome, idade=usuario_idade, escolha=usuario_opcao)

    if usuario_opcao == 1:  # quiz
        myClass.quiz()
    elif usuario_opcao == 2:    # teste dos sintomas
        myClass.lidar_com_sintomas()
    elif usuario_opcao == 3:    # Orientação para tratamentos
        myClass.tratamento_covid()
    else:
        break
