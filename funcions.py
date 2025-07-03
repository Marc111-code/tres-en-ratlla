def startBoard():
    taulell = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]
    return taulell


def drawBoard(l,n):
    if len(l) != 9:
        print('Error! Board badly designed!')
    else:
        print("Turn number:", n)
        print('='*12)
        print(' '*3 + '|'+' '*3 + '|'+' '*3)  
        print(' ' + l[6] + ' '+ '|' + ' ' + l[7]+' ' + '|'+ ' '+ l[8]+' ')
        print(' '*3 + '|'+' '*3 + '|'+' '*3)  
        print('-'*12)
        print(' '*3 + '|'+' '*3 + '|'+' '*3)  
        print(' ' + l[3] + ' '+ '|' + ' ' + l[4]+' ' + '|'+ ' '+ l[5]+' ')
        print(' '*3 + '|'+' '*3 + '|'+' '*3)   
        print('-'*12)
        print(' '*3 + '|'+' '*3 + '|'+' '*3)  
        print(' ' + l[0] + ' '+ '|' + ' ' + l[1]+' ' + '|'+ ' '+ l[2]+' ')
        print(' '*3 + '|'+' '*3 + '|'+' '*3)  
        print('='*12)



def chooseInitialPlayer():
    import random
    ran = random.randint(0,1)
    if ran == 0:
        return 'Player'
    if ran == 1:
        return 'Computer'



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
        print(jug,'occupies position',n)  
        l[n] = lletra
        return l


def isAWonPlay(l,lletra):
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
        if [6] == lletra:
            if l[7] and l[8] == lletra:
                return True
        else: 
            return False


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
    resposta = input("Choose position to play (0-8): ")
    while not(resposta >= "0" and resposta <= "8") or not(isAFreeSpace(l,int(resposta))):
        print("We are sorry. This position is not valid.")
        resposta = input("Choose position to play (0-8): ")
    return int(resposta)

def chooseLetterPlayer():
 resposta = input("Choose between X or O: ")
 while resposta != "X" and resposta != "O":
     print("We are sorry. This letter is not valid.")
     resposta = input("Choose between X or O: ")
     if resposta == "X":
        return ['X', 'O']
     if resposta == "O":
        return ['O', 'X']



def playAgain():
    resposta = input("Do you want to play another game? (y / n) ")
    while resposta != "y" and resposta != "Y" and resposta != "n" and resposta != "N":
        print("We are sorry. This option is not valid.")
        resposta = input("Do you want to play another game? (y / n) ")
    if resposta == "Y" or resposta == "y":
        return True
    if resposta == "n" or resposta == "N":
        return False  


def game():
    jug = chooseInitialPlayer()
    estatTaulell = startBoard()
    lletra = chooseLetterPlayer()
    print("Starts "+ jug)
    torn = 0
    pos = 0
    
    while not fullBoard(estatTaulell) and not isAWonPlay (estatTaulell,lletra):
        drawBoard(estatTaulell,torn)
        torn = torn + 1
        if jug =="Player":
            pos = play(estatTaulell)
            estatTaulell = applyPlay(jug,estatTaulell,lletra[0],pos)
        else:
            jug="Player"
            
       #  print(estatTaulell())
        # if chooseInitialPlayer() = "Player":
            
        
        
        
        
        
        
        
        
game()
