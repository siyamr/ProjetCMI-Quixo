import pygame, os

#Couleur menu
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

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Quixo")
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)
    pygame.display.flip()

_init_()

#Music and Audio
pygame.mixer_music.load('cmi.mp3')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.2)
son_click = pygame.mixer.Sound("bouton_son.wav")

#Global Font for All
myfont = pygame.font.SysFont('Courier', 60, bold=True)
button_font = pygame.font.SysFont('Courier', 20)
font_credits = pygame.font.SysFont('Comic Sans MS', 20, bold=True)

#Fonction écrire texte
def main_text(text, font, color, surface, x, y):
    text_object = font.render(text, 1, color)
    textrect = text_object.get_rect()
    textrect.topleft = (x, y)
    surface.blit(text_object, textrect)

#Fonction texte simple
def text_simple(text, color):
    textSurface = button_font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#Fonction texte button
def text_button(text, color, button_x, button_y, button_width, button_height):
    text_Surf, text_Rect = text_simple(text, color)
    text_Rect.center = ((button_x + (button_width / 2)), button_y + (button_height / 2))
    screen.blit(text_Surf, text_Rect)

#Fonction main
def main_menu():
    click = False
    while True:

        screen.fill(beige)
        main_text('QUIXO', myfont, white, screen, 310, 100)
        mx, my = pygame.mouse.get_pos()

        #Bouton sous la forme de Rect
        button_1 = pygame.Rect(300, 250, 200, 50)
        button_2 = pygame.Rect(300, 350, 200, 50)
        button_3 = pygame.Rect(300, 450, 200, 50)

        #Interaction souris/bouton
        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(screen, grey, button_1)
            if click:
                son_click.play()
                game()
                click = False
        else:
            pygame.draw.rect(screen, darker, button_1)

        if button_2.collidepoint((mx, my)):
            pygame.draw.rect(screen, grey, button_2)
            if click:
                son_click.play()
                rules()
                click = False
        else:
            pygame.draw.rect(screen, darker, button_2)

        if button_3.collidepoint((mx, my)):
            pygame.draw.rect(screen, grey, button_3)
            if click:
                son_click.play()
                credits()
                click = False
        else:
            pygame.draw.rect(screen, darker, button_3)

        #Texte dans les boutons
        text_button('Jouer', black, 300, 250, 200, 50)
        text_button('Règles', black, 300, 350, 200, 50)
        text_button('Crédits', black, 300, 450, 200, 50)


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

        pygame.display.update()
        mainClock.tick(60)

def game():
    click = False
    #screen = globals()["screen"]#variable local screen prend la valeur de la variable globale screen
    running = True
    while running:
        screen.fill(beige)


        main_text('Jeu', myfont, white, screen, 340, 75)
        mx, my = pygame.mouse.get_pos()

        #Bouton retour, 1v1 et 1vIA
        button_back = pygame.Rect(20, 20, 200, 25)
        button_one_v_one = pygame.Rect(250, 250, 300, 100)

        #Interaction bouton/souris
        if button_back.collidepoint((mx, my)):
            pygame.draw.rect(screen, grey, button_back)
            if click:
                return
        else:
            pygame.draw.rect(screen, darker, button_back)

        if button_one_v_one.collidepoint((mx, my)):
            pygame.draw.rect(screen, grey, button_one_v_one)
            if click:
                #vers 1v1
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
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.update()
        mainClock.tick(60)


def rules():
    click = False
    running = True
    while running:
        screen.fill(beige)

        main_text('Règles', myfont, white, screen, 290, 75)
        mx, my = pygame.mouse.get_pos()

        #Bouton Retour
        button_back = pygame.Rect(20, 20, 200, 25)

        #Interaction bouton/souris
        if button_back.collidepoint((mx, my)):
            pygame.draw.rect(screen, grey, button_back)
            if click:
                return
        else:
            pygame.draw.rect(screen, darker, button_back)

        #Texte dans le bouton
        text_button('Retour (Echap)', black, 20, 20, 200, 25)

        #Event section
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.update()
        mainClock.tick(60)

def credits():
    click = False
    running = True
    while running:
        screen.fill(beige)

        #All Credits
        main_text('Crédits', myfont, white, screen, 280, 75)
        main_text('Jeu conçu par :', font_credits, black, screen, 325, 175)
        main_text('Sofian E. | Clara L. | Adam S. | Siyam R.', font_credits, black, screen, 190, 210)
        main_text('Musique composée par :', font_credits, black, screen, 285, 300)
        main_text('Adam Said', font_credits, black, screen, 345, 335)

        mx, my = pygame.mouse.get_pos()

        #Bouton retour
        button_back = pygame.Rect(20, 20, 200, 25)

        #Interaction bouton/souris
        if button_back.collidepoint((mx, my)):
            pygame.draw.rect(screen, grey, button_back)
            if click:
                return
        else:
            pygame.draw.rect(screen, darker, button_back)

        #Texte dans le bouton
        text_button('Retour (Echap)', black, 20, 20, 200, 25)

        #Event section
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()