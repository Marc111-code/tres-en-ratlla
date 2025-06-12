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
