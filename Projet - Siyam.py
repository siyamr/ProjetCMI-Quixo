#%% Importation

from tkinter import *
import time

"""Importation des modules tkinter pour le GUI et time pour la fonction sleep (qui n'est pas utilisé ici)"""
#%% Fenetre
"""Configuration de la fenêtre"""

boutons = []
global chemin
chemin = '0'
fenetre = Tk()
fenetre.title("La forêt interdite")

#%% Histoire

histoire = {'0': {'text':"Vous vous appelez Emma. Vous avez décidé de rendre visite à votre grand-mère. \n\nNéanmoins, vos parents sont partis en vacances et vous devez traverser la forêt interdite pour arriver chez elle.",
            'Choix':{
                "Prendre le raccourci":{'suivant':'1'},
                "Continuer sur le chemin éclairé":{'suivant':'2'},
                "...":{"suivant":"1"}}},
            '1': {'text':"Pris par le temps, vous préférez prendre le chemin boueux conseillé par votre frère, défunt. \nVous continuez sur votre chemin lorsque vous entendez des bruits de pas...puis des hurlements. \n\nVous tentez de vous enfuir mais il est déjà trop tard : le Grand Méchant Loup vous voit et vous mange toute crue !","suivant":"2"},
            '2':{"text":"En continuant sur le chemin éclairé, vous avez réussi à échapper aux éventuels dangers de la forêt interdite. \n\nNéanmoins, arrivée chez votre grand-mère, vous sentez une étrange odeur... \n\n!!! \n\nLe Grand Méchant est arrivé bien avant vous, et il a dévoré votre mamie. Il ne reste plus que sa paire de lunettes... et une flaque de sang. \n\n Pris d'effroi, vous décidez de rentrer rapidement chez vous mais il fait déjà nuit...",
            'Choix':{"Réessayez":{'suivant':'0'},}},}

interaction = Label(fenetre, text=histoire.get(chemin)['text'],wraplength = 400)

interaction.pack()   

"""Stockage de l'histoire"""

#%% Fonctions

def AfficherChoix(): #Cette fonction permet d'afficher l'introduction et les différents boutons de choix
    print(chemin)
    for clef in histoire[chemin]['Choix']:
        bouton = Button(fenetre,text=clef, command = lambda: VerifierBouton(bouton))
        print(clef)
        boutons.append(bouton)
        bouton.pack()

def CreerButton(text): #Créer le bouton après le choix du joueur. Suit la fonction SansChoix
    Prochain = Button(fenetre,text=text, command = lambda: SansChoix())
    Prochain.pack()
    boutons.append(Prochain)


def SansChoix(): #Fonction qui permet d'afficher le texte suivant le choix du joueur
    for i in boutons:
        i.destroy()
    global chemin
    chemin = histoire[chemin]["suivant"]
    interaction.config(text = histoire[chemin]["text"])
    AfficherChoix()

def VerifierBouton(button): #Fonction permettant de vérifier le chemin pris par le joueur. Il permet au joueur de ne pas perdre
    global chemin
    if "Choix" in histoire[chemin] and not "suivant" in histoire[chemin]:
        chemin = histoire[chemin]["Choix"][button.config('text')[-1]]["suivant"]
        AfficherSuivant()
        if "Choix" in histoire[chemin]:
            AfficherChoix()
    if "suivant" in histoire[chemin] and not "Choix" in histoire[chemin]:
        CreerButton("Prenez l'autre chemin")

def AfficherSuivant(): #Après avoir appuyé sur un bouton, cette fonction permet d.afficher le texte suivant, selon les choix donnés
    for i in boutons:
        i.destroy()
    global chemin
    interaction.config(text=histoire[chemin]["text"])
 
#%% Fin

AfficherChoix()
fenetre.mainloop()