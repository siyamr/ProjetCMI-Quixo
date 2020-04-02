from tkinter import *
from random import randrange


# Données initiales (création d'une matrice)
def init():
    for y in range(taille):
        for x in range(taille):
            etat[x][y] = neutre
            cell[x][y] = canvas.create_rectangle((x*cote, y*cote, (x+1)*cote, (y+1)*cote), outline="black", fill="#D2B48C")

def dessiner():
        for y in range(taille):
            for x in range(taille):
                if etat[x][y]==rond:
                    canvas.create_oval(x*cote, y*cote, (x+1)*cote, (y+1)*cote,outline = 'black')
                if etat[x][y]==croix:
                    canvas.create

def rol1():
    etat[coordx][coordy]=rond
    dessiner()
    

def clic(event):
    global coordx,coord2x
    global coordy,coord2y
    if compt==0:
        coordx=(event.x)//75
        coordy=(event.y)//75
        print(coordx,coordy)
        verif()
    else :
        coord2x=(event.x)//75
        coord2y=(event.y)//75
        test()
    

def verif():
    check=False
    if coordx==0:
        check=True
    if coordx==4:
        check=True
    if (coordx==1 or coordx==2 or coordx==3) and (coordy==0 or coordy==4):
        check=True
    if check==True:
        compt=1

def test():
    etat[coordx][coordy] = vide
    check2=False
    if coordx==0:
        if coordy==0:
            if (coord2x==0 and coord2y==4) or (coord2x==4 and coord2y==0):
                check2=True
        if coordy==1 or coordy==2 or coordy==3:
            if (coord2x==0 and coord2y==0) or (coord2x==0 and coord2y==4) or (coord2x==4 and coord2y==coordy):
                check2=True
        if coordy==4:
            if (coord2x==0 and coord2y==0) or (coord2x==4 and coord2y==4):
                check2=True
    if coordx==1 or coordx==2 or coordx==3:
        if (coord2x==0 and coord2y==0) or (coord2x==4 and coord2y==0) or (coord2x==coordx and coord2y==4):
            check=True
    if coordx==4:
        if coordy==0:
            if (coord2x==0 and coord2y==0) or (coord2x==4 and coord2y==4):
                check2=True
        if coordy==1 or coordy==2 or coord2y==3:
            if (coord2x==4 and coord2y==0) or (coord2x==4 and coord2y==4) or (coord2x==0 and coord2y==coordy):
                check2=True
        if coordy==4:
            if (coord2x==0 and coord2y==4) or (coord2x==4 and coord2y==0):
                check2=True


# def mvt():
    

taille=5
cote = 75  #côté d'une cellule
neutre = 0   #piece neutre
rond=1
croix=2
compt=0
vide=3

# Matrices
cell = [[0 for i in range(taille)] for j in range(taille)]    #mémorise les cases
etat = [[neutre for i in range(taille)] for j in range(taille)] #mémorise les statuts des cases)


# Lancement du programme
fenetre = Tk()
fenetre.title("Quixo")

#Titre dans la fenêtre
texte1=Label(fenetre,text="Quixo",font=("Comic Sans MS",20,"italic"))
texte1.pack()
canvas = Canvas(fenetre, width=900, height=600)
canvas.pack()
canvas.bind("<Button>",clic)

#fonctions pour le jeu
init()
dessiner()

fenetre.mainloop()

