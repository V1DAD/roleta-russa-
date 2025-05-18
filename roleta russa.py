import random
import time
import colorama
from colorama import Fore, Back, Style
a = ''
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
cilindroplayer = [1,0,0,0,0,0]
customcilindro = False
cilpmenu = True
cilomenu = False
raridade = 1.0
capacetes = 0
capacete = False
crucifixos = 0
cruz = False
lootoutro = False
sair = False
wiki = False

txtitulo = '''
               _      _                                   
              | |    | |                                  
    _ __ ___  | | ___| |_ __ _   _ __ _   _ ___ ___  __ _ 
    | '__/ _ \| |/ _ \ __/ _` | | '__| | | / __/ __|/ _` |
    | | | (_) | |  __/ || (_| |_| |  | |_| \__ \__ \ (_| |
    |_|  \___/|_|\___|\__\__,_(_)_|   \__,_|___/___/\__,_|
                                                        
                                                        \n\n'''

while sair == False:

    
    print(Fore.RED + txtitulo + Style.RESET_ALL)
    
    menup = str(input('[1]pra jogar [w]para a wiki [s]para sair\n'))
    if menup == '1':
        a = str(input('\nvamos jogar um jogo de roleta russa s/n?\n'))
    elif menup == 'w':
        wiki = True
    elif menup == 's':
        sair = True
    else:
        print('valor inválido')

    while wiki:
        txtwiki = '''\n
Itens do jogador:
 * são dados após a vitória do jogador

    >boneco vodoo
     - quando usado se o jogador levar um tiro o outro também leva
     - pode ser negado pelo crucifixo

    >adulterador
     - faz com que o próximo tiro do outro seja verdadeiro
     
Itens do outro:
 * são dados após a vitória do jogador
 
    >crucifixo
     - nega o efeito do boneco vodoo
     - uso único

    >capacete
     - protege de uma bala
     - uso único
     
Dificuldades:

    >Fácil
     - o outro não usa itens
     - cilindro do outro: [1,1,0,0,0,0]
     - cilindor do jogador: [1,0,0,0,0,0]
     - raridade de itens do jogador: 1.0

    >Normal
     - o outro usa itens
     - multiplicador da chance do outro usar itens: 1.0
     - cilindro do outro: [1,0,0,0,0,0]
     - cilindor do jogador: [1,0,0,0,0,0]
     - raridade de itens do jogador: 1.5

    >Difícil
     - o outro usa itens
     - multiplicador da chance do outro usar itens: 1.5
     - cilindro do outro: [1,0,0,0,0,0]
     - cilindor do jogador: [1,1,0,0,0,0]
     - raridade de itens do jogador: 2.0

    >Custom
     - você decide os valores

        \n'''
        print(Style.BRIGHT + txtwiki + Style.RESET_ALL)
        sairwiki = str(input('digite qualquer coisa para sair da wiki'))
        if sairwiki == 's':
            wiki = False
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        else:
            wiki = False
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    

    #codigo das dificuldaades

    if a == 's':
        diff = str(input('\nescolha a dificuldade :\n [1]Fácil [2]Normal [3]Difícil [c]Custom\n'))
        
        if diff == '1':
            cilindro = [1,1,0,0,0,0]
        elif diff == '2':
            raridade = 1.5
            lootoutro = True
            chanceuso = 1.0
        elif diff == '3':
            cilindroplayer = [1,1,0,0,0,0]
            raridade = 2.0
            chanceuso = 1.5
            lootoutro = True
        elif diff == 'c':
            customcilindro = True
            cilindroplayer = []
            cilindro = []
            try:
                raridade = float(input('Diga qual vai ser a raridade do loot do jogador(valor padrão 1.0):\n'))
            except ValueError:
                raridade = 1.0
            lto = str(input('O outro vai ter loot também [s/n]?\n'))
            if lto == 's':
                lootoutro = True
                try:
                    chanceuso = float(input('Diga qual a chance do outro usar um item na rodada(valor padrão 1.0)'))
                except ValueError:
                    chanceuso = 1.0
    #codigo dificuldade custom
        
        while customcilindro:
            selcil = str(input('Escolha um cilindro para customizar ou digite [s] para sair:\n [1]jogador [2]outro\n'))
            if selcil == '1':
                cilpmenu = True
            elif selcil == '2':
                cilomenu = True
            elif selcil == 's':
                customcilindro = False

            while cilpmenu == True:
                cl = int(input('[1]Adicionar uma bala [0]Espaço vazio [2]Para voltar\n'))
                if cl == 0 or cl == 1:
                    cilindroplayer.append(cl)
                elif cl == 2:
                    cilpmenu = False
                print('cilindro atual: ', cilindroplayer)

            while cilomenu == True:
                cl = int(input('[1]Adicionar uma bala [0]Espaço vazio [2]Para voltar\n'))
                if cl == 0 or cl == 1:
                    cilindro.append(cl)
                elif cl == 2:
                    cilomenu = False
                print('cilindro atual: ', cilindro)

    elif a == 'n':
        print('Fim de jogo')
        
    #codigo do outro

    while a == 's':
        cilpog = cilindroplayer[:]
        ciloog = cilindro[:]

        if lootoutro == True and vitoria:
            chance = random.randint(1,int(20/raridade))
            if chance <= 4:
                capacetes = capacetes + 1
                print('o outro ganhou um capacete')
            elif chance <= 6:
                crucifixos = crucifixos + 1
                print('o outro ganhou um crucifixo')
            vitoria = False
        elif vitoria:
            vitoria = False

        if vezdele == True:
            suavez = False
            print(Fore.RED + 'minha vez\n')
            print(Style.RESET_ALL)
            roleta1 = random.choice(cilindro)
            
            uso = random.randint(1,int(20/chanceuso))
            if uso <= 2 and capacetes > 0:
                capacete = True
                capacetes = capacetes - 1
                print(Fore.RED + 'segurança em primeiro lugar')
            elif uso <= 5 and crucifixos > 0:
                cruz = True
                crucifixos = crucifixos - 1
                print(Fore.RED + 'deus me proteja' + Style.RESET_ALL)


            if adulterado == True:
                time.sleep(1)
                adulterado = False
                roleta1 = 1

            if roleta1 == 1 and capacete == False:
                time.sleep(1)
                vitoria = True
                print(Fore.YELLOW + '\nboom' + Style.RESET_ALL)
            elif  roleta1 == 1 and capacete:
                print(Fore.YELLOW + '\nboom' + Style.RESET_ALL)
                time.sleep(1)
                print(Back.WHITE + Fore.BLACK + ' o capacete quebrou ' + Style.RESET_ALL)
                time.sleep(0.5)
                suavez = True
            
            elif roleta1 == 0:
                time.sleep(1)
                print(Fore.RED + '\ntick')
                print(Style.RESET_ALL)
                time.sleep(1)
                suavez = True
                cilindro.remove(0)
            

    #codigo do player

        if suavez == True:
            vezdele = False
            menuitens = False
            print('Sua vez, o que voce quer fazer?')
            c = str(input('1[atirar] 2[usar itens] 3[desistir]\n'))
            
            if c == '1':
                roleta2 = random.choice(cilindroplayer)
                time.sleep(1)
                if roleta2 == 1 and vodoo == False:
                    print(Fore.YELLOW + '\nboom')
                    print(Style.RESET_ALL)
                    vidas = vidas - 1
                    cilindroplayer = cilpog
                    if vidas > 0:
                        vezdele = True
                        time.sleep(0.5)
                    elif vidas == 0:
                        print(Fore.RED + 'Ganhei' + Style.RESET_ALL)
                        time.sleep(0.5)
                elif roleta2 == 1 and vodoo == True:
                    print(Fore.YELLOW + '\nboom')
                    print(Style.RESET_ALL)
                    vidas = vidas - 1
                    if cruz == False:
                        print(Back.MAGENTA + Fore.BLACK + ' O boneco vodoo foi gasto,fazendo ele levar o tiro também ' + Style.RESET_ALL)
                        print(Style.RESET_ALL)
                        vodoo = False
                        vitoria = True
                        vezdele = True
                    elif cruz:
                        print(Back.LIGHTYELLOW_EX + Fore.BLACK + ' O  crucifixo protejeu o outro do boneco vodoo ')
                        vodoo = False
                        vezdele = True

                    
                else:
                    cilindroplayer.remove(0)
                    print(Fore.GREEN + '\ntick')
                    print(Style.RESET_ALL)
                    time.sleep(1)
                    vezdele = True
            if c == '2':
                menuitens = True
            
            elif c == '3':
                print('Você desistiu,sequência de vitórias: ',seqvit)
                a = 'n'

    #codigo do menu de usar itens
    
        if menuitens == True:
            suavez = False
            print(f'Quatidade de vidas: {vidas} [1]Adulteradores: {adulterador} [2]Bonecos vodoo: {bonecovodoo}')
            minput = str(input('para usar os itens digite seu numero respectivo,para sair digite qualquer outra coisa\n'))
            if minput == '1':
                if adulterador > 0:
                    adulterado = True
                    adulterador = adulterador - 1
                    print(Back.YELLOW + Fore.BLACK + ' A arma do outro foi adulterada ' + Style.RESET_ALL)
                    suavez = True
            elif minput == '2':
                if bonecovodoo > 0:
                    vodoo = True
                    bonecovodoo = bonecovodoo - 1
                    print(Back.MAGENTA + Fore.BLACK + ' O boneco não te proteje mas garante um empate ao mínimo ' + Style.RESET_ALL)
                    suavez = True
            elif minput == 'itensInfinitos':
                adulterador = 999
                bonecovodoo = 999
                print(Fore.YELLOW + '\nhaja ganância para uma pessoa só\n' + Style.RESET_ALL)
                suavez = True
            elif minput == 'sobala':
                cilindro = [1]
                cilindroplayer = [1]
                ciloog = [1]
                cilpog = [1]
                print('\nEra pra ser roleta russa mas virou suicidio coletivo agora\n')
                suavez = True
            else:
                suavez = True

    #código de vitória

        if vitoria == True and vidas > 0:
            vezdele = False
            cilindro = ciloog[:]
            seqvit = seqvit + 1
            print('você ganhou')
            
            #codigo do loot do player

            chance = random.randint(1,10 * raridade)
            if chance <= 4:
                vidas = vidas + 1
                print('Você ganhou uma vida')
            elif chance <= 6:
                bonecovodoo = bonecovodoo + 1
                print('Voce ganhou um boneco vodoo')
            elif chance == 7:
                adulterador = adulterador + 1
                print('Voce ganhou um adulterador')
            
            time.sleep(2)
            a = str(input('Quer continuar s/n?\n'))
            if a == 'n':
                print('Sequência de vitórias: ',seqvit)
            elif a == 's':
                suavez = True
            vodoo = False
        
        elif vitoria == True and vidas == 0:
            cilindro = ciloog[:]
            print('Empate, certamente uma proeza')
            time.sleep(2)
            a = str(input('Quer jogar novamente? s/n?\n'))
            if a == 'n':
                print('Sequência de vitórias: ',seqvit)
            elif a == 's':
                suavez = True
                seqvit = 0
            vodoo = False

        elif vitoria == False and vidas == 0:
            cilindro = ciloog[:]
            print('Você perdeu, sequência de vitórias: ',seqvit)
            time.sleep(0.5)
            a = str(input('Quer jogar novamente s/n?\n'))
            if a == 's':
                vidas = 1
                seqvit = 0
                suavez = False
                vezdele = True

