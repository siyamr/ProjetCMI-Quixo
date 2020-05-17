from tkinter import *
from random import randrange


# Données initiales (création d'une matrice)
def init():
    global compt
    compt = 0
    global joueur
    joueur = 1
    for y in range(taille):
        for x in range(taille):
            etat[x][y] = neutre
            cell[x][y] = canvas.create_rectangle((x * cote, y * cote, (x + 1) * cote, (y + 1) * cote), outline="black",
                                                 fill="#D2B48C")
            print(etat[x][y])


def dessiner():
    for y in range(taille):
        for x in range(taille):
            print(etat[x][y])
            if etat[x][y] == rond:
                canvas.create_oval(x * cote, y * cote, (x + 1) * cote, (y + 1) * cote, outline='black', fill='red')
            if etat[x][y] == rond2:
                canvas.create_oval(x * cote, y * cote, (x + 1) * cote, (y + 1) * cote, outline='black', fill='blue')
            if etat[x][y] == neutre:
                canvas.create_rectangle((x * cote, y * cote, (x + 1) * cote, (y + 1) * cote), outline="black",
                                        fill="#D2B48C")
    global joueur
    if joueur == 1:
        joueur = 2
    else:
        joueur = 1
    print("c'est le tour de joueur ", joueur)
    gagner()


def clic(event):
    print("compt=", compt)
    global coordx, coord2x
    global coordy, coord2y
    if compt == 0:
        coordx = (event.x) // 75
        coordy = (event.y) // 75
        print(coordx, coordy)
        verif()
    else:
        coord2x = (event.x) // 75
        coord2y = (event.y) // 75
        verif2()


def verif():
    check = False
    if coordx == 0:
        if etat[coordx][coordy] == joueur or etat[coordx][coordy] == neutre:
            check = True
    if coordx == 4:
        if etat[coordx][coordy] == joueur or etat[coordx][coordy] == neutre:
            check = True
    if (coordx == 1 or coordx == 2 or coordx == 3) and (coordy == 0 or coordy == 4):
        if etat[coordx][coordy] == joueur or etat[coordx][coordy] == neutre:
            check = True
    if check == True:
        global compt
        compt = 1
        print("le compteur à verif vaut", compt)
        if joueur == 1:
            etat[coordx][coordy] = rond
        if joueur == 2:
            etat[coordx][coordy] = rond2


def verif2():
    check2 = False
    if coordx == 0:
        if coordy == 0:
            if (coord2x == 0 and coord2y == 4) or (coord2x == 4 and coord2y == 0):
                check2 = True
        if coordy == 1 or coordy == 2 or coordy == 3:
            if (coord2x == 0 and coord2y == 0) or (coord2x == 0 and coord2y == 4) or (
                    coord2x == 4 and coord2y == coordy):
                check2 = True
        if coordy == 4:
            if (coord2x == 0 and coord2y == 0) or (coord2x == 4 and coord2y == 4):
                check2 = True
    if coordx == 1 or coordx == 2 or coordx == 3:
        if coordy == 0:
            if (coord2x == 0 and coord2y == 0) or (coord2x == 4 and coord2y == 0) or (
                    coord2x == coordx and coord2y == 4):
                check2 = True
        if coordy == 4:
            if (coord2x == 0 and coord2y == 4) or (coord2x == 4 and coord2y == 4) or (
                    coord2x == coordx and coord2y == 0):
                check2 = True
    if coordx == 4:
        if coordy == 0:
            if (coord2x == 0 and coord2y == 0) or (coord2x == 4 and coord2y == 4):
                check2 = True
        if coordy == 1 or coordy == 2 or coord2y == 3:
            if (coord2x == 4 and coord2y == 0) or (coord2x == 4 and coord2y == 4) or (
                    coord2x == 0 and coord2y == coordy):
                check2 = True
        if coordy == 4:
            if (coord2x == 0 and coord2y == 4) or (coord2x == 4 and coord2y == 0):
                check2 = True
    if check2 == True:
        mvt()
    else:
        print("Vous ne pouvez pas jouer ici")


def mvt():
    var = etat[coordx][coordy]
    if coord2x == coordx:
        y = coord2y
        if coord2y == 0:
            while y <= coordy:
                if y == 0:
                    stock2 = etat[coord2x][y]
                    etat[coord2x][y] = var
                else:
                    stock = etat[coord2x][y]
                    etat[coord2x][y] = stock2
                    stock2 = stock
                y = y + 1
        else:
            while y >= coordy:
                if y == 4:
                    stock2 = etat[coord2x][y]
                    etat[coord2x][y] = var
                else:
                    stock = etat[coord2x][y]
                    etat[coord2x][y] = stock2
                    stock2 = stock
                y = y - 1

    if coord2y == coordy:
        x = coord2x
        if coord2x == 0:
            while x <= coordx:
                if x == 0:
                    stock2 = etat[x][coord2y]
                    etat[x][coord2y] = var
                else:
                    stock = etat[x][coord2y]
                    etat[x][coord2y] = stock2
                    stock2 = stock
                x = x + 1
        else:
            while x >= coordx:
                if x == 4:
                    stock2 = etat[x][coord2y]
                    etat[x][coord2y] = var
                else:
                    stock = etat[x][coord2y]
                    etat[x][coord2y] = stock2
                    stock2 = stock
                x = x - 1
    dessiner()
    global compt
    compt = 0


def gagner():
    cptj1 = 0
    cptj2 = 0
    partie = False
    for y in range(taille):
        cptj1=0
        for x in range(taille):
            if etat[x][y]==rond:
                cptj1=cptj1+1
                if cptj1 == 5:
                    popup()
    for y in range(taille):
        cptj2=0
        for x in range(taille):
            if etat[x][y]==rond2:
                cptj2=cptj2+1
                if cptj2 == 5:
                    popup()
    for x in range(taille):
        cptj1=0
        for y in range(taille):
            if etat[x][y]==rond:
                cptj1=cptj1+1
                if cptj1==5:
                    popup()
    for x in range(taille):
        cptj2=0
        for y in range(taille):
            if etat[x][y]==rond2:
                cptj2=cptj2+1
                if cptj2==5:
                    popup()
    if (etat[0][0] == etat[1][1] == etat[2][2] == etat[3][3] == etat[4][4]) and etat[0][0] != neutre:
        partie = True
    if (etat[4][0] == etat[3][1] == etat[2][2] == etat[1][3] == etat[0][4]) and etat[4][0] != neutre:
        partie = True
        if partie == True:
            popup()


def popup():
    fen1 = Tk()
    tex1 = Label(fen1, text='Vous avez gagné !', fg='red')
    tex1.pack()
    bou1 = Button(fen1, text='Quitter', command=fen1.destroy)
    bou1.pack()
    fen1.mainloop()


taille = 5
cote = 75  # côté d'une cellule
neutre = 0  # piece neutre
rond = 1
rond2 = 2

# Matrices
cell = [[0 for i in range(taille)] for j in range(taille)]  # mémorise les cases
etat = [[neutre for i in range(taille)] for j in range(taille)]  # mémorise les statuts des cases)

# Lancement du programme
fenetre = Tk()
fenetre.title("Quixo")

# Titre dans la fenêtre
texte1 = Label(fenetre, text="Quixo", font=("Comic Sans MS", 20, "italic"))
texte1.pack()
canvas = Canvas(fenetre, width=375, height=400)
canvas.pack()
canvas.bind("<Button>", clic)

# fonctions pour le jeu
init()
dessiner()
b1 = Button(fenetre, text='Restart', command=init)
b1.pack(side=TOP, padx=3, pady=3)

fenetre.mainloop()
