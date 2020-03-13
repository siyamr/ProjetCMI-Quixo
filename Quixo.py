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
                    cavans.create

def rol1():
    etat[coordx][coordy]=rond
    dessiner()
    

def clic(event):
    global coordx
    global coordy
    coordx=(event.x)//75
    coordy=(event.y)//75
    print(coordx,coordy)
    verif()

def verif():
    check=False
    if coordx==0:
        check=True
    if coordx==4:
        check=True
    if (coordx==1 or coordx==2 or coordx==3) and (coordy==0 or coordy==4):
        check=True
    if check==True:
        rol1()
            
taille=5
cote = 75  #côté d'une cellule
neutre = 0   #piece neutre
rond=1
croix=2

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
