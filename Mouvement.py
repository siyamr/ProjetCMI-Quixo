
import Quixo.py
case[X] = ?         #case jouée avec des coordonnées en x et y
global mvt = ""     #Endroit ou la case est déplacée G,D,B,H
# petit "x"  = coordonné en abscisse  petit "y" = coordonné en ordonné   grand "X" = case jouée (combinaison de "x" et "y" à déterminer)

#--------Définitions fonctions----------#


def verifInput():
    while (mvt != 'G' or mvt != 'D' or mvt != 'B' or mvt != 'H'):
        print("Entré invalide, veuillez choisir l'une des propositions ci-contre [G]auche, [D]roite, [B]as, [H]aut")
        mvt = input()
        mvt = mvt.upper()


def depgauche():    # Déplacement case jouée à gauche
    tmp = case[X]
    for i in range(x,0):
        if i-1 < 0:
            case[0] = tmp
            break
        case[i] = case[i-1]

def depdroite():    # Déplacement case jouée à droite
    tmp = case[X]
    for i in range(x,4):
        if i+1 > 4:
            case[4] = tmp
            break
        case[i] = case[i+1]

def depbas():    # Déplacement case jouée en bas
    tmp = case[X]
    for i in range(y,4):    # y = la coordonnée en ordonné
        if i+1 > 4:
            case[4] = tmp
            break
        case[i] = case[i+1]


def dephaut():    # Déplacement case jouée en haut
    tmp = case[X]
    for i in range(y,0):
        if i-1 < 0:
            case[0] = tmp
            break
        case[i] = case[i-1]


def direction():
    if mvt == "G":
        if x!=0:    # x = coordonné en x (abscisse)
            depgauche()
        else:
            while mvt == "G":
                print("Vous êtes déja de ce côté du plateau.\n Choissisez une autre direction. D ; B ; H")
                mvt = input()
                verifInput()
                direction()
    elif mvt == "D":
        if x!=4:    # x = coordonné en x (abscisse)
            depdroite()
        else:
            while mvt == "D":
                print("Vous êtes déja de ce côté du plateau.\n Choissisez une autre direction. G ; B ; H")
                mvt = input()
                verifInput()
                direction()

    elif mvt == "B":
        if y!=4:    # x = coordonné en x (abscisse)
            depbas()
        else:
            while mvt == "B":
                print("Vous êtes déja de ce côté du plateau.\n Choissisez une autre direction. G ; D ; H")
                mvt = input()
                verifInput()
                direction()

    else:
        if y!=0:    # x = coordonné en x (abscisse)
            dephaut()
        else:
            while mvt == "H":
                print("Vous êtes déja de ce côté du plateau.\n Choissisez une autre direction. D ; B ; H")
                mvt = input()
                verifInput()
                direction()



#-----------Programme-----------#

print("Ou voullez-vous déplacer la case ? [G,D,B,H]")
str mvt = input()
mvt = mvt.upper()

verifInput()


direction()
