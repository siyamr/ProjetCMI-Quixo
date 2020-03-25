import Quixo.py
global case[x] = 1 #case jouée [0-15]
global mvt = "" #Endroit ou la case est déplacée G,D,B,H


def depgauche():

def depdroite():
    global tmp = case[x]
    case[x] = 3
    for i in range(1, 5):
        if case[i] == 3:
            break
        if x + i > 4:
            case[0]= case[x]
        else :
            case[x + i] = tmp


def depbas():

def dephaut():



def direction():
    if mvt == "G":
        depgauche
    elif mvt == "D":
        depdroite
    elif mvt == "B":
        depbas
    else:
        dephaut


print("Ou voullez-vous déplacer la case ? [G,D,B,H]")
str mvt = input()
mvt = mvt.upper()


while (mvt != 'G' or mvt != 'D' or mvt != 'B' or mvt != 'H'):
    print("Entré invalide, veuillez choisir l'une des propositions ci-contre [G]auche, [D]roite, [B]as, [H]aut")
    mvt = input()
    mvt = mvt.upper()

direction
