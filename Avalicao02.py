import random

def menu():
  print(50*"-")

  print("---AVALIAÇÃO ALGORITMO E LÓGICA DE PROGRAMAÇÃO---")
  
  print("\n1 - PERCORRER PALAVRA")
  print("2 - JOGO DA QUINA")
  print("9 - FINALIZAR")

  escolha = int(input("\nOpção desejada: "))
  return(escolha)

enter = ''
opcao = 0


def palavra():
    palavra1 = str(input("\nInsira palavra desejada: ")).upper()
    num = 0

    for i in palavra1:
        num = num + 1
        print("\nLetra da Palavra:", i, " - POSIÇÃO: ", num)
        print("Posição no Alfabeto:", ord(i) - 64)
        print(40*"-")

    enter = input("\nPressione ENTER para Prosseguir!")        
    return(menu)

def jogoquina():
    print('\n', 40*"-")
    print("JOGO DA QUINA 2021!")
    print(40*"-")

    apost = ''
    sort = ''
    acert = ''
    nro_acertos = 0
    list_apost = []
    list_sort = []

    for i in range(5):
        numero_apostado = random.randrange(60)
        list_apost.append(numero_apostado)

        if i < 4:
            apost = apost+str(numero_apostado) + ' - '

        else:
            apost = apost+str(numero_apostado)

        ###################################################
        numero_sorteado = random.randrange(60)
        list_sort.append(numero_sorteado)

        if i < 4:
            sort = sort+str(numero_sorteado) + ' - '
        
        else:
            sort = sort+str(numero_sorteado)

        acertou = []
        for ap in list_apost:
            for sor in list_sort:
                if  ap ==  sor:
                    if ap not in acertou:
                        acertou.append(ap)

    for atc in acertou:
        acertos = 'ACERTOU! -> Nº APOSTADO: ' + str(atc) + ' - Nº SORTEADO: ' + str(atc) + '\n'
        acert =  acert + acertos
        nro_acertos =  nro_acertos + 1
        

    print("Números Apostados:")
    print(apost)

    print("\nNúmeros Sorteados:")
    print(sort)

    print("\nAcertos:")
    print(acert)

    print("\nNúmeros de acertos:")
    print(nro_acertos)
    
    enter = input("\nPressione ENTER para Prosseguir!")  

# MENU PRINCIPAL
while opcao != 9:
    opcao = menu()
    
    if(opcao == 1):
        palavra()
        

    elif(opcao == 2):
        
        jogoquina()

    elif(opcao == 9):
        print('PROGRAMA FINALIZADO!')
        break
    else:
        print("Opção Inválida")
        enter = input("\nPressione ENTER para Prosseguir!")