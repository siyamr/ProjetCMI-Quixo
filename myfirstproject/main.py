import pygame, os

#Couleur menu/texte
beige = (255, 224, 163)
white = (255, 255, 255)
grey = (192, 192, 192)
darker = (170, 170, 170)
black = (0, 0, 0)

#Variables
running = True
screen = ()
mainClock = None

#Fenetre du jeu
def _init_():
    pygame.init()
    if not "screen" in globals() :
       global mainClock, screen
    mainClock = pygame.time.Clock()
    #Initialisation de l'écran, du titre et de l'icone de la fenêtre
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Quixo")
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)
    pygame.display.flip()

_init_()

#Music and Audio
pygame.mixer_music.load('cmi.mp3')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.3)
son_click = pygame.mixer.Sound("bouton_son.wav")
rules_quixo = pygame.image.load('regles.png')


#Toutes les polices pour le texte
main_font = pygame.font.SysFont('Courier', 60, bold=True)
button_font = pygame.font.SysFont('Courier', 20)
font_credits = pygame.font.SysFont('Comic Sans MS', 20, bold=True)
font_rules = pygame.font.SysFont('Calibri', 20, bold=True)

#Fonction écrire un texte
def main_text(text, font, color, surface, x, y):
    text_object = font.render(text, 1, color)
    textrect = text_object.get_rect()
    textrect.topleft = (x, y)
    surface.blit(text_object, textrect)

#Fonction texte nécessaire pour la fonction text_button
def text_simple(text, color):
    textSurface = button_font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#Fonction text_button
def text_button(text, color, button_x, button_y, button_width, button_height):
    text_Surf, text_Rect = text_simple(text, color)
    text_Rect.center = ((button_x + (button_width / 2)), button_y + (button_height / 2))
    screen.blit(text_Surf, text_Rect)

#Fonction main, le menu du jeu
def main_menu():
    click = False
    while True:
        #Ecran en couleur beige, on récupère également les données de la position de la souris
        screen.fill(beige)
        main_text('QUIXO', main_font, white, screen, 310, 100)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        #Création de bouton avec Rect
        button_play = pygame.Rect(300, 250, 200, 50)
        button_rules = pygame.Rect(300, 350, 200, 50)
        button_credits = pygame.Rect(300, 450, 200, 50)
        button_quit = pygame.Rect(550, 450, 50, 50)

        #Interaction souris/bouton, rend le bouton plus clair quand la souris passe dessus.
        #Vers Jouer
        if button_play.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, grey, button_play)
            if click:
                son_click.play()
                game()
                click = False
        else:
            pygame.draw.rect(screen, darker, button_play)
        #vers Règles
        if button_rules.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, grey, button_rules)
            if click:
                son_click.play()
                rules()
                click = False
        else:
            pygame.draw.rect(screen, darker, button_rules)
        #vers Credits
        if button_credits.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, grey, button_credits)
            if click:
                son_click.play()
                credits()
                click = False
        else:
            pygame.draw.rect(screen, darker, button_credits)
        #Quitter
        if button_quit.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, grey, button_quit)
            if click:
                pygame.quit()
        else:
            pygame.draw.rect(screen, darker, button_quit)

        #Texte dans les boutons
        text_button('Jouer', black, 300, 250, 200, 50)
        text_button('Règles', black, 300, 350, 200, 50)
        text_button('Crédits', black, 300, 450, 200, 50)
        text_button('x', black, 550, 450, 50, 50)

        #Event sections
        for event in pygame.event.get():
            #Event = Quit
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Fermeture du jeu")
            #Event = Echap
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            #Event = Click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
        #Maintien de la fenêtre à jour
        pygame.display.update()
        mainClock.tick(60)

#Fonction game, pour jouer au jeu
def game():
    click = False
    running = True
    while running:
        #Ecran en couleur beige, on récupère également les données de la position de la souris
        screen.fill(beige)
        main_text('Jeu', main_font, white, screen, 340, 75)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        #Bouton retour, 1v1 et 1vIA
        button_back = pygame.Rect(20, 20, 200, 25)
        button_one_v_one = pygame.Rect(250, 250, 300, 100)

        #Interaction souris/bouton, rend le bouton plus clair quand la souris passe dessus.
        #Retour au menu
        if button_back.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, grey, button_back)
            if click:
                return
        else:
            pygame.draw.rect(screen, darker, button_back)
        #vers 1v1
        if button_one_v_one.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, grey, button_one_v_one)
            if click:
                #vers le jeu Quixo sur Tkinter
                son_click.play()
                pygame.display.iconify()
                os.system("python -u quixo.py")
                # en dessous, fenetre tkinter fermé, reprise de l'execution de la fenetre pygame
                click = False
        else:
            pygame.draw.rect(screen, darker, button_one_v_one)

        #Texte dans les boutons
        text_button('Retour (Echap)', black, 20, 20, 200, 25)
        text_button('1 contre 1', black, 250, 250, 300, 100)

        #Event section
        for event in pygame.event.get():
            #Event = Quit
            if event.type == pygame.QUIT:
                pygame.quit()
            #Event = Echap pour revenir au menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            #Event = Click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
        #Maintien de la fenêtre à jour
        pygame.display.update()
        mainClock.tick(60)

#Fonction rules, liste des règles du jeu Quixo
def rules():
    click = False
    running = True
    while running:

        screen.fill(beige)

        #Toutes les règles
        screen.blit(rules_quixo, (585, 385))
        main_text('Règles', main_font, white, screen, 290, 75)
        main_text('But du Jeu :', font_rules, darker, screen, 345, 175)
        main_text('• Réaliser un alignement de 5 cubes à l’horizontal,', font_rules, black, screen, 195, 210)
        main_text('   à la vertical ou en diagonal avec votre symbole.', font_rules, black, screen, 195, 230)
        main_text('Déroulement :', font_rules, darker, screen, 335, 280)
        main_text('• En début de partie, les 25 cases du jeu sont remplies avec des pions "blancs".', font_rules, black, screen, 70, 315)
        main_text("• A tour de rôle, prenez l'un des 16 pions situés sur le contour du plateau,", font_rules, black, screen, 70, 345)
        main_text('   de votre symbole choisi au départ ou un pion "blanc".', font_rules, black, screen, 70, 365)
        main_text("• On ne peut pas prendre un pion ayant le symbole de l'adversaire.", font_rules, black, screen, 15, 395)
        main_text('• Le pion saisi doit être replacé sur l’une des extrémités du', font_rules, black, screen, 15, 425)
        main_text('   plateau, sur une rangée incomplète créée lors du choix du pion.', font_rules, black, screen, 15, 445)
        main_text('• Le pion ne peut pas être reposé sur la case où il a été pris.', font_rules, black, screen, 15, 475)
        main_text("• La partie se termine lorsque l'un des joueurs réalise", font_rules, black, screen, 15, 505)
        main_text("   un alignement de 5 pions.", font_rules, black, screen, 15, 525)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        #Bouton Retour
        button_back = pygame.Rect(20, 20, 200, 25)

        #Interaction souris/bouton, rend le bouton plus clair quand la souris passe dessus.
        #Retour au menu
        if button_back.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, grey, button_back)
            if click:
                return
        else:
            pygame.draw.rect(screen, darker, button_back)

        #Texte dans le bouton
        text_button('Retour (Echap)', black, 20, 20, 200, 25)

        #Event section
        for event in pygame.event.get():
            #Event = Quit
            if event.type == pygame.QUIT:
                pygame.quit()
            #Event = Echap pour revenir au menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            #Event = Click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
        #Maintien de la fenêtre à jour
        pygame.display.update()
        mainClock.tick(60)

#Fonction credits, tous les crédits du jeu
def credits():
    click = False
    running = True
    while running:

        screen.fill(beige)

        #Tous les crédits
        main_text('Crédits', main_font, white, screen, 280, 75)
        main_text('Jeu conçu par :', font_credits, black, screen, 325, 175)
        main_text('Sofian E. | Clara L. | Adam S. | Siyam R.', font_credits, black, screen, 190, 210)
        main_text('Musique composée par :', font_credits, black, screen, 285, 300)
        main_text('Adam Said', font_credits, black, screen, 345, 335)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        #Bouton retour
        button_back = pygame.Rect(20, 20, 200, 25)

        #Interaction bouton/souris,
        if button_back.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, grey, button_back)
            if click:
                return
        else:
            pygame.draw.rect(screen, darker, button_back)

        #Texte dans le bouton
        text_button('Retour (Echap)', black, 20, 20, 200, 25)

        #Event section
        for event in pygame.event.get():
            #Event = Quit
            if event.type == pygame.QUIT:
                pygame.quit()
            #Event = Echap pour revenir au menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            #Event = Click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
        #Maintien de la fenêtre à jour
        pygame.display.update()
        mainClock.tick(60)

main_menu()