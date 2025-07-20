def startBoard():
    taulell = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    return taulell


def drawBoard(l,n):
    if len(l) != 9:
        print('Error! Board badly designed!')
    else:
        print("Número de torn", n)
        print('='*12)
        print(' ' + l[0] + ' '+ '|' + ' ' + l[1]+' ' + '|'+ ' '+ l[2]+' ')
        print('-'*12)
        print(' ' + l[3] + ' '+ '|' + ' ' + l[4]+' ' + '|'+ ' '+ l[5]+' ')
        print('-'*12)
        print(' ' + l[6] + ' '+ '|' + ' ' + l[7]+' ' + '|'+ ' '+ l[8]+' ')
        print('='*12)



def chooseInitialPlayer():
    import random
    ran = random.randint(0,1)
    if ran == 0:
        return 'Jugador'
    if ran == 1:
        return 'Ordinador'



def isAFreeSpace(l,n):
    if n >=len(l):
        return False
    if l[n] == ' ':
        return True
    else:
        return False


def fullBoard(l):
    i = 0
    while i < len(l):
        if l[i] == ' ':
            return False
        i = i + 1
    return True


def applyPlay(jug,l,lletra,n):
        print(jug,'ocupa la posició',n)  
        l[n] = lletra
        return l

def isAWonPlay(l, lletra):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for combo in winning_combinations:
        if all(l[i] == lletra for i in combo):
            return True
    return False
'''def isAWonPlay(l,lletra):
        if l[0] == lletra:
            if l[1] and l[2] == lletra:
                return True
            if l[3] and l[6] == lletra:
                return True
            if l[4] and l[8] == lletra:
                return True
        if l[1] == lletra:
            if l[4] and l[7] == lletra:
                return True
        if l[2] == lletra:
            if l[5] and l[8] == lletra:
                return True
            if l[4] and l[6] == lletra:
                return True
        if l[3] == lletra:
            if l[4] and l[5] == lletra:
                return True
        if l[6] == lletra:
            if l[7] and l[8] == lletra:
                return True
        else: 
            return False

'''
import random
def randomPlay(l):
    c = 0
    b = []
    for element in l:
        if element == " ":
            b = b + [c]
        c = c + 1
    if len(b) == 0:
        return "-1"
    return random.choice(b)


def play(l):
    resposta = input("Tria posició per jugar (0-8): ")
    while not(resposta >= "0" and resposta <= "8") or not(isAFreeSpace(l,int(resposta))):
        print("Ho sentim. Aquesta posició no és vàlida")
        resposta = input("Tria posició per jugar (0-8): ")
    return int(resposta)

def chooseLetterPlayer():
 resposta = input("Tria entre X o O: ")
 while resposta != "X" or resposta != "O":
     print("Ho sentim. Aquesta lletra no està disponible.")
     resposta = input("Tria entre X o O: ")
     if resposta == "X":
        return ['X', 'O']
     else:
        return ['O', 'X']



def playAgain():
    resposta = input("Vols jugar una altre partida? (s / n) ")
    while resposta != "s" and resposta != "S" and resposta != "n" and resposta != "N":
        print("Ho sentim. Aquesta opció no és vàlida.")
        resposta = input("Vols jugar una altre partida? (s / n) ")
    if resposta == "Y" or resposta == "y":
        return True
    if resposta == "n" or resposta == "N":
        return False  


def game():
    jug = chooseInitialPlayer()
    estatTaulell = startBoard()
    lletra = chooseLetterPlayer()
    print("Comença "+ jug)
    torn = 0
    pos = 0
    while not fullBoard(estatTaulell) and not isAWonPlay (estatTaulell,lletra[0]) and  not isAWonPlay (estatTaulell,lletra[1]):
        drawBoard(estatTaulell,torn)
        
        torn = torn + 1
        if jug == "Jugador":
            pos = play(estatTaulell)
            estatTaulell = applyPlay(jug, estatTaulell, lletra[0], pos)
            jug = "Ordinador"
        else:
            pos = randomPlay(estatTaulell)
            estatTaulell = applyPlay(jug, estatTaulell, lletra[1], pos)
            
            jug = "Jugador"
    if isAWonPlay(estatTaulell, lletra[0]):
        print("Molt Bé, Has Guanyat!")
        playAgain()
    elif isAWonPlay(estatTaulell, lletra[1]):
        print("L'Ordinador ha guanyat!")
        playAgain()
    else:
        print("Empat! El tauler està ple i ningú ha guanyat.")
        playAgain()
game()
