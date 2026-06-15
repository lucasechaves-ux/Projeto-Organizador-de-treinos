treinos = []

#cadastra as sessões
def cadastrar_treino():
    nome = str(input("😁 Entre com o nome do seu treino 😁:  "))
    exercício = str(input("🏋️ Digite o exercício que será realizado 🏋️: "))
    series = int(input("🔢 Digite o número de series 🔢: "))
    repetições = int(input('🔂 Digite o número de repetições desse exercício 🔂: '))
    dia = str(input("🗓️ Digite qual o dia da semana será seu treino 🗓️: "))

    treino = { # dicionario organiza os dados
        "nome": nome,
        "exercício": exercício,
        "series": series,
        "repetições": repetições,
        "dia": dia,
        "realizado": False

    }
    treinos.append(treino)
    print("✅ Sessão cadastrada com sucesso! ✅\n")#\n pula uma linha

def consultar_treinos():
    if len(treinos) == 0:
        print("😢 Você não possui sessões cadastradas! 😢\n")
        return #serve para sair da função
    numero = 1 # lista as sessões cadastradas
    for treino in treinos: #percorre a lista, mostrando as sessões cadastradas
        status = " " #define se esta realizada ou não
        if treino['realizado']==True: #mostra de forma visual se esta realizada ou não
            status = '✅ Realizado'
        else: #mostra de forma visual se esta realizada ou não
            status = '❌ Não Realizado'

        print(f'[{numero}] Nome: {treino ['nome']} | Exercício: {treino ['exercício']} | '
              f'Series: {treino ['series']} | Repetições: {treino ['repetições']} | Dia: {treino ['dia']} | '
              f'Status: {status}\n') # mostra as sessões cadastradas de forma visual e organizada
        numero += 1 #lista as sessões 1,2,3,4....

    print() #serve para separar as informações

def buscar_treinos():
    termo = str(input('🔍 Busque por treino ou dia da semana 🔎: ')).lower()
    encontrados = [] #serve para armazenar as sessões encontradas

    for treino in treinos: #percorre a lista
        if (termo in treino['nome'].lower()) or (termo in treino['dia'].lower()): #verifica se encontra a sessão por dia ou por tema
            encontrados.append(treino) #adiciona as sessão encontradas na variavel composta encontrados

    if len(encontrados) == 0: # se não houver nenhuma sessão encontrada ele retorna o print abaixo
        print('😢 Nenhuma sessão encontrada! 😢')
        return #sai da condição

    numero = 1  # lista as sessões cadastradas
    for treino in treinos:  # percorre a lista, mostrando as sessões cadastradas
        status = " "  # define se esta realizada ou não
        if treino['realizado'] == True:  # mostra de forma visual se esta realizada ou não
            status = '✅ Realizado'
        else:  # mostra de forma visual se esta realizada ou não
            status = '❌ Não Realizado'

        print(f'[{numero}] Nome: {treino['nome']} | Exercício: {treino['exercício']} | '
              f'Series: {treino['series']} | Repetições: {treino['repetições']} | Dia: {treino['dia']} | '
              f'Status: {status}\n')  # mostra as sessões cadastradas de forma visual e organizada
        numero += 1  # lista as sessões 1,2,3,4....

def marcar_treino_como_realizado():
    consultar_treinos()
    if len(treinos) == 0:
        return
    else:
        numero = int(input('Digite o número do treino que você deseja marcar como realizada: '))
        indice = numero - 1
        if numero <= len(treinos):
            treinos[indice]['realizado'] = True
            print('✅ Treino marcado como Realizado! ✅\n')
        else:
            print('⚠️ Número inválido. ⚠️\n')

def editar_treinos():
    consultar_treinos()
    if len(treinos) == 0:
        return
    else:
      numero = int(input('✏️ Digite o número do treino que deseja editar : '))
      indice1 = numero - 1

    if numero > len(treinos) or numero <= 0:
        print('⚠️ Número inválido. ⚠️\n')
        return

    print('\n🔄 Digite os novos dados do treino 🔄\n')

    treinos[indice1]['nome'] = input('😁 Novo nome do treino 😁: ')
    treinos[indice1]['exercício'] = input('🏋️ Novo exercício 🏋️: ')
    treinos[indice1]['series'] = int(input('🔢 Novo número de séries 🔢: '))
    treinos[indice1]['repetições'] = int(input('🔂 Novo número de repetições 🔂: '))
    treinos[indice1]['dia'] = input('🗓️ Novo dia da semana 🗓️: ')

    print('✅ Treino editado com sucesso! ✅\n')

def remover_treinos():
    consultar_treinos()
    if len(treinos) == 0: return
    else:
        escolher = int(input('⚠️ Escolha qual treino você deseja remover ⚠️: '))
        num = escolher - 1
        if escolher <= len (treinos):
            treinos.pop(num)
            print('✅ Treino Removido com Sucesso! ✅\n')
        else:
            print('⚠️ Número inválido. ⚠️\n')

def exibir_menu():
    while True: #mostrar as opções do sistema quantas vezes forem necessarias
        print('=== Organizador de treinos! ===')
        print('1. 📝 Cadastrar novo treino 📝')
        print('2. 🗒️ Consultar treinos 🗒️')
        print('3. 🔍 Buscar por treino ou dia 🔍')
        print('4. ✅ Marcar treino como realizado ✅')
        print('5. 🔂 Editar seus treinos 🔂')
        print('6. ❌ Remover um treino ❌')
        print('7. Sair')
        escolha = str(input('Escolha uma opção: '))
        if escolha == '1':
            cadastrar_treino()
        elif escolha == '2':
            consultar_treinos()
        elif escolha == '3':
            buscar_treinos()
        elif escolha == '4':
            marcar_treino_como_realizado()
        elif escolha == '5':
            editar_treinos()
        elif escolha == '6':
            remover_treinos()
        elif escolha == '7':
            print('👋 Saindo do Sistema. Até a próxima!👋')
            break
        else: # se caso o usuario digitar algo alem do 1,2,3,4,5.
            print('⚠️ Opção inválida. Tente novamente! ⚠️')

exibir_menu()
