from random import randrange
import time
from math import ceil

argent = 1000
continue_jeu = True


def miser():
    global nbr_mise
    nbr_mise = -1
    while nbr_mise < 0 or nbr_mise > 49:
        nbr_mise = input("Sur quelle case voulez-vous miser (0 - 49) ?")
        try:
            nbr_mise = int(nbr_mise)
        except ValueError:
            print("Ce n'est pas un nombre valide")
            nbr_mise = -1
            continue
        if nbr_mise < 0 or nbr_mise > 49:
            print("Ce n'est pas un nombre valide")
    return nbr_mise

def pari(argent):
    global nbr_pari
    nbr_pari =-1
    while nbr_pari < 0 or nbr_pari > argent:
        nbr_pari = input("Combien voulez-vous miser ?")
        try:
            nbr_pari = int(nbr_pari)
        except ValueError:
            print("Ce n'est pas un nombre valide")
            nbr_pari = -1
            continue
        if nbr_pari < 0:
            print("Mise un peu plus !")
            nbr_pari = -1
        elif nbr_pari > argent:
            print("T'as pas assez !")
            nbr_pari = -1
    return nbr_pari


print("Vous arrivez au casino avec ", argent, "$")

while continue_jeu:

    print("Vous avez ",argent,"$ en poche.\n")
    miser()
    print("Vous misez sur le ", nbr_mise, "!\n Validez-vous cette mise ? [y/n]")
    val1 = input()
    while val1 != 'y':
        miser()
        print("Vous misez sur le ", nbr_mise, "!\n Validez-vous cette mise ? [y/n]")
        val1 = input()
    print("Case validée ! Votre case : le", nbr_mise)

    pari(argent)
    print("Vous pariez ", nbr_pari, "Cela vous convient-il ? [y/n]")
    val2 = input()
    while val2 != 'y':
        pari(argent)
        print("Vous pariez ", nbr_pari, "Cela vous convient-il ? [y/n]")
        val2 = input()
    print("Mise validée ! Vous jouez ", nbr_pari,"$ sur le ",nbr_mise,"!")

    pointe = randrange(50)
    print("La roulette est lancée ...")
    time.sleep(3)
    print("Ca tourne !")
    time.sleep(2)
    print("Elle ralentie...")
    time.sleep(2)
    print("... Et s'arrête sur le...")
    time.sleep(2)
    print(pointe)

    if pointe == nbr_mise:
        print("Félicitations ! Vous obtenez", nbr_mise * 3, "$ !")
        argent += nbr_mise * 3
    elif pointe % 2 == nbr_mise % 2:  # ils sont de la même couleur
        nbr_mise = ceil(nbr_mise * 0.5)
        print("Vous avez misé sur la bonne couleur. Vous obtenez", nbr_mise, "$")
        argent += nbr_mise
    else:
        print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
        argent -= nbr_mise

    print("Voulez-vous continuer à jouer ? [y/n]")  # Quitter le jeu
    byebye = input()
    if byebye != 'y':
        continue_jeu = False
        print("A bientôt...")
    else:
        print("Super !")
