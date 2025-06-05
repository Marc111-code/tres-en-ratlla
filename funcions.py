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
