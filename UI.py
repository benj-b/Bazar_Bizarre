#Binome : Amiard Antoine / Benjamin Bernaud

import turtle as t
import math as m
import time
import drawings
import random

#Fonction qui va tout mettre en place
def main_setup():
    #on modifie le nom de la fenetre
    t.title("Bazar Bizarre !")
    #et on met en place les different elements
    bgScreen = setup_bg()
    #scoreScreen = setup_score()
    drawingScreen = setup_drawing()
    warningScreen = setup_warning()
    buttonsScreen = setup_buttons()

    #et on renvoie les objet pour des modifications dans le programme principal
    return bgScreen, drawingScreen, warningScreen, buttonsScreen

#Fonction qui va preparer le tout pour les dessins et afficher les regles du jeu
def setup_drawing():
    #on cree un nouvel objet Trutle
    screen = t.Turtle()
    #on cache le curseur
    screen.ht()
    #on modife la vitesse d'ecriture
    screen.speed(0)
    #on change la couleur du stylo
    screen.pencolor('white')
    return screen

#Fonctions qui affiche le menu principale
def setup_main_menu():
    #on modifie la vitesse, la couleur, la grosseur, etc...
    t.setup(1900, 700)
    screen = t.Turtle()
    screen.ht()
    screen.speed(0)
    drawings.move_wo_draw(screen, 0, 300)
    screen.pencolor("white")
    screen.pensize(3)
    screen.write("BAZAR BIZARRE", align="center", font=("Vintage", 26, "normal"))
    screen.fillcolor("midnight blue")

    #on dessine les 3 boutons 
    for ycor in [-200, 0, 200]:
        drawings.move_wo_draw(screen, -150, ycor)
        for loop in range(2):
            screen.begin_fill()
            screen.fd(300)
            screen.right(90)
            screen.fd(125)
            screen.right(90)
            screen.end_fill()  

    #on ecrit dans ces boutons        
    drawings.move_wo_draw(screen, 0, 100)
    screen.write("Lancer\nune\npartie", align="center", font=("Arial", 18, "normal"))
    drawings.move_wo_draw(screen, 0, -100)
    screen.write("Règles\ndu\njeu", align="center", font=("Arial", 18, "normal"))
    drawings.move_wo_draw(screen, 0, -275)
    screen.write("Options", align="center", font=("Arial", 18, "normal"))
    """drawings.move_wo_draw(screen, -600, -290)
    screen.write("Menu", align="center", font=("Arial", 18, "normal"))"""

    return screen

#Fonction qui affiche le boutton pour quitter et ne va jamais etre effacé
def setup_leave_button():
    #on creer un nouvel objet Turtle et on modife, la taille, la couleur du stylo, etc...
    screen = t.Turtle()
    screen.ht()
    screen.pencolor("white")
    screen.fillcolor("midnight blue")
    screen.pensize(2)
    drawings.move_wo_draw(screen, 550, -250)
    #on dessine le bouton
    for loop in range(2):
        screen.begin_fill()
        screen.fd(100)
        screen.right(90)
        screen.fd(75)
        screen.right(90)
        screen.end_fill()
    drawings.move_wo_draw(screen, 600, -300)
    #on ecrit dans le bouton
    screen.write("Quitter", align="center", font=("Arial", 18, "normal"))
    return screen

#Fonction qui affiche le bouton pour retourner au menu
def return_menu_button():
    #Cette fonction a le même principe que celle pour le bouton quitter
    screen = t.Turtle()
    screen.ht()
    screen.pencolor("white")
    screen.fillcolor("midnight blue")
    screen.pensize(2)
    drawings.move_wo_draw(screen, -650, -250)
    for loop in range(2):
        screen.begin_fill()
        screen.fd(100)
        screen.right(90)
        screen.fd(75)
        screen.right(90)
        screen.end_fill()
    drawings.move_wo_draw(screen, -600, -300)
    screen.write("Menu", align="center", font=("Arial", 18, "normal"))
    return screen

#fonction qui va affiche
def setup_options():
    screen = t.Turtle()
    screen.ht()
    screen.speed(0)
    screen.pencolor("gold")
    screen.pensize(3)
    screen.fillcolor("dim gray")

    #On dessine pour indiquer les parametre de jeu
    for ycor in [120, -80]:
        
        drawings.move_wo_draw(screen, -520, ycor)
        screen.begin_fill()
        for loop in range(2):
            screen.fd(840)
            screen.right(90)
            screen.fd(165)
            screen.right(90)
        screen.end_fill()
        

    screen.fillcolor("midnight blue")
    screen.pencolor("white")

    
    drawings.move_wo_draw(screen,0,300)
    screen.write("Options", align="center", font=("Vintage", 26, "underline"))

    #on dessine les boutons
    for ycor in [-100, 100]:
        drawings.move_wo_draw(screen, -500, ycor)
        for loop in range(2):
            screen.begin_fill()
            screen.fd(300)
            screen.right(90)
            screen.fd(125)
            screen.right(90)
            screen.end_fill()

    #on ecrit dedans
    drawings.move_wo_draw(screen,-350,10)
    screen.write("Difficulté", align='center',font=('Arial',26,'normal'))
    drawings.move_wo_draw(screen,-350,-220)
    screen.write("Temps\nde\ndépart", align='center',font=('Arial',26,'normal'))

    for xcor in [-100, 50, 200]:
        drawings.move_wo_draw(screen, xcor, 75)
        for loop in range(2):
            screen.begin_fill()
            screen.fd(100)
            screen.right(90)
            screen.fd(75)
            screen.right(90)
            screen.end_fill()

        drawings.move_wo_draw(screen, xcor, -125)
        for loop in range(2):
            screen.begin_fill()
            screen.fd(100)
            screen.right(90)
            screen.fd(75)
            screen.right(90)
            screen.end_fill()

    #on ecrit dans ces boutons
    drawings.move_wo_draw(screen,-50,30)
    screen.write("Facile", align='center',font=('Arial',18,'normal'))
    drawings.move_wo_draw(screen, 100,30)
    screen.write("Moyen", align='center',font=('Arial',18,'normal'))
    drawings.move_wo_draw(screen,250,30)
    screen.write("Difficile", align='center',font=('Arial',18,'normal'))
    drawings.move_wo_draw(screen,-50,-170)
    screen.write("15s", align='center',font=('Arial',18,'normal'))
    drawings.move_wo_draw(screen,100,-170)
    screen.write("30s", align='center',font=('Arial',18,'normal'))
    drawings.move_wo_draw(screen,250,-170)
    screen.write("60s", align='center',font=('Arial',18,'normal'))
    
    return screen
    
    
#fonctions qui met en place l'arriere plan du menu
def setup_bg_menu():
    screen = t.Turtle()
    screen.ht()
    sc = screen.getscreen()
    sc.bgcolor("midnight blue")
    sc.tracer(200)
    #on dessine les etoiles pour l'arriere plan
    pair = 0
    for y in range(-400, 400, 50):
        for x in range(-950, 950, 100):
            #si la ligne est pair, on decale l'etoile de 50
            if pair%2 == 0:
                x += 50

            drawings.star(screen, x, y, "gold", 10)

            pair += 1
    return screen

#Fonctions qui affiche les règles
def rules():
    screen = t.Turtle()
    screen.ht()
    screen.pensize(2)
    screen.pencolor("gold")
    screen.fillcolor('dim gray')
    drawings.move_wo_draw(screen,-700,200)
    #on dessine un carré gris pour plus de lisibilité des regles
    for loop in range(2):
            screen.begin_fill()
            screen.fd(1400)
            screen.right(90)
            screen.fd(300)
            screen.right(90)
            screen.end_fill()

    #on affiche les regles
    screen.pencolor("white")
    drawings.move_wo_draw(screen, 0, 150)
    screen.write("Règles du jeu : ", align = 'center',font=("Arial", 26, "underline"))
    drawings.move_wo_draw(screen, 0, 110)
    screen.write("Il existe 5 formes de couleurs differentes -> {0}".format(", ".join(["{} {}".format(i, l) for (i, l) in zip(drawings.formes, drawings.couleurs)])), align = 'center', font=('Arial', 18, 'bold'))
    drawings.move_wo_draw(screen, 0, 70)
    screen.write("Une carte va être tirée avec 2 formes et 2 couleurs différentes", align = 'center', font=('Arial', 18, 'bold'))
    drawings.move_wo_draw(screen, 0, 30)
    screen.write("Si une des 2 formes est un pion qui existe alors il faut cliquer sur le bouton du pion", align='center', font=("Arial", 18, "bold"))
    drawings.move_wo_draw(screen, 0, -10)
    screen.write("Sinon il faut cliquer sur le bouton du pion n'ayant aucun point commun avec les 2 formes et couleurs", align='center', font=("Arial", 18, "bold"))
    drawings.move_wo_draw(screen, 0, -50)
    screen.write("Cliquez pour revenir au menu principal...", align='center', font=("Arial", 18, "bold"))

    #et on retourne l'objet
    return screen


    
#Fonction qui va mettre en place l'arriere plan
def setup_bg():
    #on cree un nouvel objet Turtle
    screen = t.Turtle()
    #on cache le curseur
    screen.ht()
    #on modifie la vitesse d'ecriture
    screen.speed(0)
    #on recupere l'ecran et on change la couleur de l'arriere plan
    sc = screen.getscreen()
    sc.bgcolor("midnight blue")
    sc.tracer(4000)

    #on dessine un arriere plan pour le menu
    pair = 0
    for y in range(-450, 450, 50):
        for x in range(-950, 950, 100):
            #si la ligne est pair, on decale l'etoile de 50
            if pair%2 == 0:
                x += 50
            
            drawings.star(screen, x, y, "gold", 10)

        pair += 1

    pair = 0

    #on voulait dessiner des lunes mais l'optimisation ne le permet pas
    """for y in range(-485, 480, 50):
        for x in range(-940, 920, 100):
            if pair%2 == 1:
                x += 50
                
            drawings.moon(screen, x, y, "gray", 1/8)

        pair += 1"""

    #on dessine par dessus un carré noir permettant de mieux voir les dessins
    screen.right(screen.heading())
    drawings.move_wo_draw(screen,-525, 175)
    screen.pencolor("gold")
    screen.fillcolor("black")
    screen.begin_fill()
    for loop in range(2):
        screen.fd(1050)
        screen.right(90)
        screen.fd(325)
        screen.right(90)
        
    screen.end_fill()
                   
                
    #on retourne l'objet
    return screen


#Fonctions qui va afficher si la personne a juste ou non
def display_rep(screen, bool_rep):
    screen.up()
    screen.goto(0, 100)
    #si la reponse est juste, on affiche quelque chose
    if bool_rep:
        screen.pencolor("green")
        screen.write("Bonne réponse !", align='center', font=("Arial", 18, 'normal'))
    #sinon on affiche autre chose
    if not bool_rep:
        screen.pencolor("red")
        screen.write("Mauvaise réponse !", align='center', font=("Arial", 18, 'normal'))
    screen.clear()
    

#Fonction qui va mettre en place le boutons
def setup_buttons():
    #on cree un nouvel objet Trutle
    screen = t.Turtle()
    #on modifie la vitesse d'ecriture
    screen.speed(0)
    #on cache le curseur
    screen.ht()
    #on modifie la taille du stylo
    screen.pensize(3)
    #on modifie la couleur du stylo
    screen.pencolor('white')
    screen.fillcolor("midnight blue")
    listCoor = [-350, -200, -50, 100, 250]
    #on dessine les boutons
    for loop in listCoor:
        drawings.move_wo_draw(screen, loop, -200)
        screen.begin_fill()
        drawings.polygone(screen, 4, 100)
        screen.end_fill()

    #On affiche les dessins dans les boutons
    drawings.star(screen, -300, -240, drawings.turtleColors[0], 40)
    drawings.ovni(screen, -196, -260, drawings.turtleColors[1], 1/2.5)
    drawings.satellite(screen, -10, -235, drawings.turtleColors[2],1, 1/4)
    drawings.flake(screen, 147, -250, drawings.turtleColors[3], 1/3)
    drawings.rocket(screen, 300, -300, drawings.turtleColors[4],2, 1/3)

    return screen

#Fonction qui met tout en place pour le message d'avertisement lorsque le joueur clique pas sur un bouton
def setup_warning():
    screen = t.Turtle()
    screen.up()
    screen.ht()
    screen.goto(0, 250)
    screen.pencolor("white")
    screen.down()
    
    return screen

#Fonction pour afficher le message d'averissement
def display_warning(screen):
    screen.undo()
    screen.write("Veuillez cliquer sur un bouton", align='center', font=("Arial", 12, "normal"))
    
#Fonction qui affiche les dessins de la carte (CFD = Coordinates First Drawing, CSD = Coordinates Scond Drawing)
def draw_card(card, turtleForms, turtleColors, screen, listCFD, listCSD):
    
    #si la variable card contient 2 élément alors la carte est un pion existant
    if len(card) == 2:
        intTemp = [0, 1, 2, 3, 4]
        intTemp.remove(card[0])
        formeA = random.choice(intTemp)
        intTemp.remove(formeA)
        couleurA = random.choice(intTemp)
        card = list(card)
        card.append(formeA)
        card.append(couleurA)
        card = tuple(card)

    #on recupere les coordonnées des 2 bon pions dans la liste
    CFD = listCFD[card[0]]
    CSD = listCSD[card[2]]
    x = CFD[0]
    y = CFD[1]
    #on les dessine
    for i in range(0, len(card),2):
        argForm = card[i]
        argColor = card[i+1]
        turtleForms[argForm](screen, x, y, turtleColors[argColor])
        x = CSD[0]
        y = CSD[1]

#Fonction qui affiche un ecran apres une victoire
def win(time):
    winScreen = t.Turtle()
    winScreen.ht()
    winScreen.pencolor("White")
    drawings.move_wo_draw(winScreen,0,110)
    winScreen.write("Bien joué !", align='center', font=("Arial", 20, "normal"))
    drawings.move_wo_draw(winScreen,0,70)
    winScreen.write("Fin de la partie !",align='center', font=("Arial", 20, "normal"))
    drawings.move_wo_draw(winScreen,0,30)
    winScreen.write("Vous avez tenu {} secondes".format(time), align='center', font=("Arial", 20, "normal"))
    drawings.move_wo_draw(winScreen,0,-10)
    winScreen.write("Cliquez pour revenir au menu",align='center', font=("Arial", 20, "normal"))
    return winScreen


