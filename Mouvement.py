# Recevoir les cases disponibles pour jouer
global coordonne
global possibilite
possibilite =  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def coord_input():
    coordonne = 0
    print("Entrez les coordonnés de la case que vous voulez jouer")
    x = input()
    y = input()
    while x < 0 or x > 4:
        print("Coordonné en x invalide")
        x = input()
    while y < 0 or y > 4:
        print("Coordonné en y invalide")
        y = input()
    coordonne = x + y  # transforme les coordonnés en un couple pour vérifier sa disponibilité
    return coordonne



def mvt():
    coord_input()
    for i in range(len(possibilite)):
