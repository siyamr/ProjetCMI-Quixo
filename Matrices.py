from tkinter import *
from random import randrange


# Données initiales (création du plan de jeu grâce à la matrice)
def init():
    for y in range(taille):
        for x in range(taille):
            etat[x][y] = neutre
            cell[x][y] = canvas.create_rectangle((x*cote, y*cote, (x+1)*cote, (y+1)*cote), outline="black", fill="white")

            
taille = 5  #tailleeur du tableau
cote = 75  #côté d'une cellule
neutre = 0   #case blanche


# Matrices
cell = [[0 for i in range(taille)] for j in range(taille)]    #mémorise les carrés qui représentent cases
etat = [[neutre for i in range(taille)] for j in range(taille)] #mémorise les statuts des cases

# Lancement du programme
fenetre = Tk()
fenetre.title("Quixo")

#Titre dans la fenêtre
canvas = Canvas(fenetre, width=900, height=600)
canvas.pack()

#fonctions pour lancer le Quixo
init()

fenetre.mainloop()
