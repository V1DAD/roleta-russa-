import random
import time
a = str(input('vamos jogar um jogo de roleta russa s/n?'))
while a == 's':
    print('minha vez')
    time.sleep(2)
    b = random.randint(1,6)
    if b == 1:
        a = 'n'
        print('boom,você ganhou')
    else:
        print('tick')
        c = str(input('Sua vez, quer desistir s/n?'))
        time.sleep(3)
        if c == 'n':
            b = random.randint(1,6)
            if b == 1:
                a = 'n'
                print('boom,você perdeu')
            else:
                print('tick')
                time.sleep(2)
        else:
           print('Você perdeu')
