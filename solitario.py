import random
import os

os.system("")


def PrepareGame(game,deck):
    index=0
    for i in range (len (game)):
        for j in range (i,len(game)):
            card=deck[index]
            game[j].append(card)
            index+=1
    return game,deck[index:]


def Limpiar():
    os.system('cls' if os.name=='nt' else 'clear')


def PrintCard(card):
    if card[3]==1:
        return '🂠'
    if card[0]=='H' or card[0]=='D':
        return f"\033[31m{card[2]}\033[0m"
    return f"\033[0m{card[2]}\033[0m"


def PrintGame(game,cursor):
    print ("  ", end="|")
    for n in Orden:
        print (PrintCard(n[-1]) if n[-1][1]>0 else ' ', end="|")
    print ("   mazo:", '🂠' if deck else ' ', len(deck), end="  ")
    if select1==DESCARTE:
        print ("\033[32m", end="")
    print ("descarte:", PrintCard(Descarte[-1]) if Descarte else ' ', "\033[0m")
    print("")
    for n,(i,c) in enumerate(zip(game, cursor)):
        print(c, end="  ")
        if i:
            i[-1][3]=0
        if select1==n:
            print ("\033[32m",end="")
        for j in i:
            print(PrintCard(j), end=" ")
        if select1==n:
            print ("\033[0m",end="")
        print(" ")


def PuedeIr(carta,destino):
    if not destino:
        return carta[1]==13
    ultima=destino[-1]
    if ultima[3]==1 or ultima[1]!=carta[1]+1:
        return False
    return (carta[0] in ('S','C')) != (ultima[0] in ('S','C'))


def CheckCards():
    for i in game[select1]:
        if i[3]==0 and PuedeIr(i,game[select2]):
            return i
    return None


def AFundacion(carta):
    for i in Orden:
        if carta[0]==i[-1][0] and carta[1]-1==i[-1][1]:
            i.append(carta)
            return True
    return False


def Robar():
    global deck
    if deck:
        carta=deck.pop()
        carta[3]=0
        Descarte.append(carta)
    else:
        for carta in Descarte:
            carta[3]=1
        deck=Descarte[::-1]
        Descarte.clear()


def Victoria():
    return all(len(i)==14 for i in Orden)


deck=[['S',1,'🂡',1],['S',2,'🂢',1],['S',3,'🂣',1],['S',4,'🂤',1],['S',5,'🂥',1],['S',6,'🂦',1],['S',7,'🂧',1],['S',8,'🂨',1],['S',9,'🂩',1],['S',10,'🂪',1],['S',11,'🂫',1],['S',12,'🂭',1],['S',13,'🂮',1],
      ['H',1,'🂱',1],['H',2,'🂲',1],['H',3,'🂳',1],['H',4,'🂴',1],['H',5,'🂵',1],['H',6,'🂶',1],['H',7,'🂷',1],['H',8,'🂸',1],['H',9,'🂹',1],['H',10,'🂺',1],['H',11,'🂻',1],['H',12,'🂽',1],['H',13,'🂾',1],
      ['C',1,'🃑',1],['C',2,'🃒',1],['C',3,'🃓',1],['C',4,'🃔',1],['C',5,'🃕',1],['C',6,'🃖',1],['C',7,'🃗',1],['C',8,'🃘',1],['C',9,'🃙',1],['C',10,'🃚',1],['C',11,'🃛',1],['C',12,'🃝',1],['C',13,'🃞',1],
      ['D',1,'🃁',1],['D',2,'🃂',1],['D',3,'🃃',1],['D',4,'🃄',1],['D',5,'🃅',1],['D',6,'🃆',1],['D',7,'🃇',1],['D',8,'🃈',1],['D',9,'🃉',1],['D',10,'🃊',1],['D',11,'🃋',1],['D',12,'🃍',1],['D',13,'🃎',1]]
game=[[],[],[],[],[],[],[]]
cursor=['☞',' ',' ',' ',' ',' ',' ']
Orden=[[['S',0,' ',1]],[['H',0,' ',1]],[['C',0,' ',1]],[['D',0,' ',1]]]
Descarte=[]
NADA,DESCARTE=7,8
select1,select2=NADA,NADA
mensaje=""

random.shuffle(deck)
game,deck=PrepareGame(game,deck)


while True:
    Limpiar()
    PrintGame(game,cursor)
    if Victoria():
        print("\nHas ganado!")
        input("Pulsa enter para salir")
        break
    print(mensaje)
    mensaje=""
    move=input("w/s cursor · d mover · a fundación · r robar · e descarte · q salir: ").lower()
    pos=cursor.index('☞')
    if move=='s':
        cursor.insert(0,cursor.pop())
    elif move=='w':
        cursor.append(cursor.pop(0))
    elif move=='r':
        Robar()
        select1=NADA
    elif move=='e':
        select1=DESCARTE if Descarte and select1!=DESCARTE else NADA
    elif move=='q':
        break
    elif move=='d':
        if select1==NADA:
            if game[pos]:
                select1=pos
        elif select1==pos:
            select1=NADA
        elif select1==DESCARTE:
            if PuedeIr(Descarte[-1],game[pos]):
                game[pos].append(Descarte.pop())
            else:
                mensaje="Movimiento no valido"
            select1=NADA
        else:
            select2=pos
            carta1=CheckCards()
            if carta1 is None:
                mensaje="Movimiento no valido"
            else:
                corte=game[select1].index(carta1)
                game[select2].extend(game[select1][corte:])
                del game[select1][corte:]
            select1,select2=NADA,NADA
    elif move=='a':
        if select1==DESCARTE:
            if AFundacion(Descarte[-1]):
                Descarte.pop()
            else:
                mensaje="No va a la fundación"
        else:
            origen=select1 if select1!=NADA else pos
            if game[origen] and AFundacion(game[origen][-1]):
                game[origen].pop()
            else:
                mensaje="No va a la fundación"
        select1=NADA
