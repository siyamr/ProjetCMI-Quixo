from tkinter import *
from random import randrange


# Données initiales (création d'une matrice)
def init():
    global compt
    compt=0
    global joueur
    joueur=1
    for y in range(taille):
        for x in range(taille):
            etat[x][y] = neutre
            cell[x][y] = canvas.create_rectangle((x*cote, y*cote, (x+1)*cote, (y+1)*cote), outline="black", fill="#D2B48C")
            print(etat[x][y])

def dessiner():
        for y in range(taille):
            for x in range(taille):
                print(etat[x][y])
                if etat[x][y]==rond :
                    canvas.create_oval(x*cote, y*cote, (x+1)*cote, (y+1)*cote,outline = 'black')
                if etat[x][y]==croix:
                    canvas.create_line(coordx,coordy,coordx+1,coordy+1, fill = 'black')
                if etat[x][y] == neutre:
                    canvas.delete(canvas.create_oval(x*cote, y*cote, (x+1)*cote, (y+1)*cote,outline = 'black'))
        global joueur
        if joueur == 1:
            joueur = 2
        else :
            joueur = 1
        print("c'est le tour de joeur ",joueur)
                    
def gagner():
    cptj1=0
    cptj2=0
    while cptj1!=5 or cptj2!=5:
        for y in range(taille):
            cptj1=0
            cptj2=0
            for x in range(taille):
                if etat[x][y]==rond:
                    cptj1=cptj1+1
                if etat[x][y]==croix:
                    cptj2=cptj2+1
        for x in range(taille):
            cptj1=0
            cptj2=0
            for y in range(taille):
                if etat[x][y]==rond:
                    cptj1=cptj1+1
                if etat[x][y]==croix:
                    cptj2=cptj2+1   

def clic(event):
    print("compt=",compt)
    global coordx,coord2x
    global coordy,coord2y
    if compt==0 :
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
        global compt
        compt=1
        print("le compteur à verif vaut",compt)
        if joueur == 1:
            etat[coordx][coordy]=rond
        if joueur == 2 :
            etat[coordx][coordy]=croix

def test():
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
        if coordy==0:
            if (coord2x==0 and coord2y==0) or (coord2x==4 and coord2y==0) or (coord2x==coordx and coord2y==4):
                check2=True
        if coordy==4:
            if (coord2x==0 and coord2y==0) or (coord2x==4 and coord2y==4) or (coord2x==coordx and coord2y==0):
                check2=True
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
    if check2==True :
        mvt()
    else :
        print("Vous ne pouvez pas jouer ici")


def mvt():
    var=etat[coordx][coordy]
    if coord2x==coordx:
        y=coord2y
        if coord2y==0:
            while y <= coordy:
                if y==0:
                    stock2=etat[coord2x][y]
                    etat[coord2x][y]=var
                else :
                    stock=etat[coord2x][y]
                    etat[coord2x][y]=stock2
                    stock2=stock
                y=y+1
        else :
            while y>= coordy:
                if y==4:
                    stock2=etat[coord2x][y]
                    etat[coord2x][y]=var
                else :
                    stock=etat[coord2x][y]
                    etat[coord2x][y]=stock2
                    stock2=stock
                y=y-1

    if coord2y==coordy:
        x=coord2x
        if coord2x==0:
            while x<= coordx:
                if x==0:
                    stock2=etat[x][coord2y]
                    etat[x][coord2y]=var
                else :
                    stock=etat[x][coord2y]
                    etat[x][coord2y]=stock2
                    stock2=stock
                x=x+1
        else :
            while x>= coordx:
                if x==4:
                    stock2=etat[x][coord2y]
                    etat[x][coord2y]=var
                else :
                    stock=etat[x][coord2y]
                    etat[x][coord2y]=stock2
                    stock2=stock
                x=x-1
    dessiner()
    global compt
    compt=0
    gagner()
    
    

taille=5
cote = 75  #côté d'une cellule
neutre = 0   #piece neutre
rond=1
croix=2
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
b1 = Button(fenetre, text ='restart', command =init)
b1.pack(side =LEFT, padx =3, pady =3)

fenetre.mainloop()
