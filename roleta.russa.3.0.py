import random
import time
import colorama
from colorama import Fore, Back, Style
suavez = False
vezdele = True
vitoria = False
vidas = 1
adulterador = 0
adulterado = False
bonecovodoo = 0
vodoo = False
seqvit = 0
menuitens = False
cilindro = [1,0,0,0,0,0]

print(Style.RESET_ALL)

a = str(input('vamos jogar um jogo de roleta russa s/n?\n'))

if a == 's':
	diff = int(input('escolha a dificuldade dando um numero, quanto maior o numero menor a chance de  você morrer:\n'))
elif a == 'n':
    print('Fim de jogo')
else:
    print('valor invalido')

while a == 's':
    if vezdele == True:
        suavez = False
        print(Fore.RED + 'minha vez')
        print(Style.RESET_ALL)
        roleta1 = random.choice(cilindro)
        #print(roleta1)

        if adulterado == True:
            time.sleep(1)
            adulterado = False
            roleta1 = 1

        if roleta1 == 1:
            time.sleep(1)
            vitoria = True
            print(Fore.YELLOW + '\nboom' + Style.RESET_ALL)
        elif roleta1 == 0:
            time.sleep(1)
            print(Fore.RED + 'tick')
            print(Style.RESET_ALL)
            time.sleep(1)
            suavez = True
            cilindro.remove(0)
    
    if suavez == True:
        vezdele = False
        menuitens = False
        print('Sua vez, o que voce quer fazer?')
        c = str(input('1[atirar] 2[usar itens] 3[desistir]\n'))
        
        if c == '1':
            roleta2 = 0
            roleta2 = random.randint(1,diff)
            #print(roleta2)
            time.sleep(1)
            if roleta2 == 1 and vodoo == False:
                print(Fore.YELLOW + '\nboom')
                print(Style.RESET_ALL)
                vidas = vidas - 1
                if vidas > 0:
                    vezdele = True
            elif roleta2 == 1 and vodoo == True:
                print(Fore.YELLOW + '\nboom')
                print(Style.RESET_ALL)
                vidas = vidas - 1
                print(Back.RED + Fore.BLACK + 'O boneco vodoo foi gasto,fazendo ele levar o tiro também' + Style.RESET_ALL)
                print(Style.RESET_ALL)
                vodoo = False
                vitoria = True
                
            else:
                print(Fore.GREEN + '\ntick')
                print(Style.RESET_ALL)
                time.sleep(1)
                vezdele = True
        if c == '2':
            menuitens = True
        
        elif c == '3':
           print('Você desistiu,sequência de vitórias: ',seqvit)
           a = 'n'
    
    if menuitens == True:
        suavez = False
        print(f'Quatidade de vidas: {vidas} [1]Adulteradores: {adulterador} [2]Bonecos vodoo: {bonecovodoo}')
        minput = str(input('para usar os itens digite seu numero respectivo,para sair digite qualquer outra coisa\n'))
        if minput == '1':
            if adulterador > 0:
                adulterado = True
                adulterador = adulterador - 1
                suavez = True
        elif minput == '2':
            if bonecovodoo > 0:
                vodoo = True
                bonecovodoo = bonecovodoo - 1
                suavez = True
        elif minput == 'itensInfinitos':
            adulterador = 999
            bonecovodoo = 999
            suavez = True
   
    if vitoria == True and vidas > 0:
        vezdele = False
        cilindro = [1,0,0,0,0,0]
        seqvit = seqvit + 1
        print('você ganhou')
        
        chance = random.randint(1,10)
        if chance >= 4:
            vidas = vidas + 1
            print('Você ganhou uma vida')
        elif chance == 7:
            adulterador = adulterador + 1
            print('Voce ganhou um adulterador')
        elif chance == 6 or 5:
            bonecovodoo = bonecovodoo + 1
            print('Voce ganhou um boneco vodoo')
        
        time.sleep(2)
        a = str(input('Quer continuar s/n?\n'))
        if a == 'n':
            print('Sequência de vitórias: ',seqvit)
        elif a == 's':
            vezdele = True
        vitoria = False
    
    elif vitoria == True and vidas == 0:
        cilindro = [1,0,0,0,0,0]
        print('Empate, certamente uma proeza')
        time.sleep(2)
        a = str(input('Quer jogar novamente? s/n?\n'))
        if a == 'n':
            print('Sequência de vitórias: ',seqvit)
        elif a == 's':
            vezdele = True
            seqvit = 0
        vitoria = False

    elif vitoria == False and vidas == 0:
        cilindro = [1,0,0,0,0,0]
        print('Você perdeu, sequência de vitórias: ',seqvit)
        time.sleep(1)
        a = str(input('Quer jogar novamente s/n?\n'))
        if a == 's':
            vidas = 1
            seqvit = 0