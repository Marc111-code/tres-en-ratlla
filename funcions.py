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
