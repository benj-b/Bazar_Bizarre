#Binome : Amiard Antoine / Benjamin Bernaud 

import random
import time
import os
import UI
import math as m
import drawings


mainScreen = UI.t.getscreen()
UI.t.ht()
#on definit les variables globales utiles pour la fonction 'clicked' puis les initialise
card = None
count = 10
secondCount = None
totalTime = None
buttonActivated = True
drawing = False
#la variable "difficulty" est une liste avec en premier le nombre de seconde gagné pour une bonne reponse et le deuxieme indice pour le nombre de seconde perdu pour une mauvaise réponse
difficulty = [7, 4]
continueC = None

#Fonction qui va generer une carte
def generate_card(nbPion=2):
    nbPion = int(nbPion * 2)
    #on verifie la probabilté de piocher un pion existant
    if random.randint(0, 8) == 5:
        randInt = random.randrange(0, nbPion)
        #on prend un pion existant
        card = [randInt, randInt]

    else:
        #on crée une liste temporaire pour faciliter la création de la carte
        intTemp = range(0, nbPion + 1)
        intTemp = list(intTemp)
        
        card = []
        #on a besoin de créer 2 couleurs et 2 formes aléatoires différentes
        for i in range(0 , nbPion):
            #on choisi un entier aléatoirement parmi les chiffres de la liste 'IntTemp'
            randInt = random.choice(intTemp)
            #on l'ajoute a la liste qui sera la carte
            card.append(randInt)
            #puis on supprime cet entier de la liste 'IntTemp' pour ne pas le reutiliser
            intTemp.remove(randInt)

    return tuple(card)

#Fonction qui va verifier le reponse du joueur
def check_rep(repPlayer, card):
    #on enleve 1 à la réponse du joueur pour se mettre dans le même comptage que le language (commence à 0)
    repPlayer -= 1
    #si le nombre d'élèments dans le tuple est égal à 2, le pion à entrer est celui de la carte
    if len(card) == 2:
        #on verifie alors si l'entrée est correct
        if repPlayer in card:
            return True

        else:
            return False

    #si le nombre d'élèments dans le tuple est égal à 4, le pion à entrer est donc différent de ceux sur la carte
    if len(card) == 4:
        #si le pion n'a rien en commun avec la carte alors la reponse est vraie
        if repPlayer not in card:
            return True
        
        else:
            return False

#fonction qui va verifier si le joueur clique sur le bouton quitter
def verif_leave(x , y):
    if y >= -325 and y <= -250:
        if x <= 650 and x >= 550:
            #si le joueur a clique, on ferme le jeu
            mainScreen.bye()
            return True
        else:
            return False

    else:
        return False

#fonction qui va verifier si le joueur clique sur le bouton menu
def verif_menu(x, y):
    global secondCount
    global totalTime
    global count
    global continueC
    global displayWin
    
    if y >= -325 and y <= -250:
        if x >= -650 and x <=    -550:
            #si le joueur a cliqué, on arrete le timer, reinitialise et on retourne au menu
            continueC = False
            secondCount = 0
            displayWin = False
            return_menu(x, y)
            return True
        else:
            return False
    else:
        return False
    
#Fonction qui va verifier si le joueur clique sur un bouton
def get_click(x, y):

    if verif_menu(x, y):
        repPlayer = -1

    elif verif_leave(x, y):
        repPlayer = -1
    
    #on verifie que le joueur ait bien cliqué sur un bouton
    elif y <= -200 and y >= -300:
        if x >= -350 and x <= -250:
            repPlayer = 1
        elif x >= -200 and x <= -100:
            repPlayer = 2
        elif x >= -50 and x <= 50:
            repPlayer = 3
        elif x >= 100 and x <= 200:
            repPlayer = 4
        elif x >= 250 and x <= 350:
            repPlayer = 5
        else:
            repPlayer = None


    else:
        repPlayer = None

    #renvoie la valeur de la reponse du joueur
    return repPlayer

#Fonction pour decrementer le timer  
def countdown():
    global secondCount
    global buttonActivated
    global timerScreen
    global totalTime
    global continueC
    global displayWin

    #si le timer n'est pas fini
    if secondCount > 0:
        #On efface le dernier nombre
        timerScreen.undo()
        mainScreen.ontimer(countdown, 1000)
        #on affiche le numéro
        timerScreen.write(secondCount, align='center', font=('Arial', 20, 'normal'))

    #si le timer est fini
    if secondCount <= 0:
        if displayWin:
            #on efface l'ecran pour dessiner 
            drawingScreen.clear()
            win()
        
    if continueC:
        secondCount -= 1

#Fonction qui va jouer le role de timer
def timer(count):
    global buttonActivated
    global timerScreen
    global secondCount

    secondCount = count
    #on cree un nouvel objet Trutle
    timerScreen = UI.t.Turtle()
    #on modifie la couleur du stylo
    timerScreen.pencolor('white')
    #on cache le curseur
    timerScreen.ht()
    #on modifie la vitesse d'ecriture
    timerScreen.speed(0)
    timerScreen.up()
    #on se deplace au coordonnée indiqué
    timerScreen.goto(0, 300)
    #on ecrit le score
    timerScreen.write("Temps restant :", align = 'center', font=("Arial", 20, "normal"))
    timerScreen.goto(120, 300)
    timerScreen.down()
    mainScreen.ontimer(countdown, 1000)

#Fonction qui va afficher les regles lorsque qu'on click sur le regles dans le menu principal
def rules():
    global rulesScreen
    #Si on clique on lance la fonction clickedRules
    mainScreen.onclick(clickedRules)
    rulesScreen = UI.rules()

#Fonction qui va faire revenir au menu principal
def clickedRules(x, y):
    global rulesScreen

    rulesScreen.clear()

    
    main_menu()
    
#Fonction qui va afficher le menu des options
def options():
    global optionsScreen
    global count
    global menuButtonScreen

    
    mainScreen.onclick(clickedOptions)
    #on affiche le bouton pour revenir au menu
    menuButtonScreen = UI.return_menu_button()
    #on affiche les options
    optionsScreen = UI.setup_options()

#Fonction qui va faire revenir au menu principal
def clickedOptions(x,y):
    global optionsScreen
    global difficulty
    global count

    verif_leave(x, y)
    if verif_menu(x, y):
        optionsScreen = None
    #On verifie où clique l'utilisateur, on modifiera alors la difficulté, le temps de départ ou on retournera au menu ou on quittera
    if y<=75 and y>=0:
        if x >= -100 and x <= 0:
            difficulty = [10, 2]
        if x >= 50 and x <= 150:
            difficulty = [7, 4]
        if x >= 200 and x <= 300:
            difficulty = [5, 5]

    if y<=-125 and y>=-200:
        if x >= -100 and x <= 0:
            count = 15
        if x >= 50 and x <= 150:
            count = 30
        if x >= 200 and x <= 300:
            count = 60

#fonctions qui retourne l'utilisateur au menu
def return_menu(x, y):
    global optionsScreen
    global returnScreen
    global drawingScreen
    global timerScreen
    global warningScreen

    #on verifie s'il clique sur quitter seulement pour l'ecran de fin une fois gagné
    verif_leave(x, y)

    #on essaye d'effacer les options
    try:
        optionsScreen.clear()

    #s'il y a une erreur, alors le joueur est en partie, donc on efface toute la partie
    except:
        #on desactive puis reactive le bouton pendant ce temps la
        buttonActivated = False
        mainScreen.clear()
        bgMenuScreen = UI.setup_bg_menu()
        timerScreen.clear()
        warningScreen.clear()
        buttonActivated = True

    #on retourne au menu
    menuButtonScreen.clear()
    main_menu()
    
#Fonction qui construit le menu principal
def main_menu():
    global mainMenuScreen
    global winScreen
    global bgScreen
    global buttonActivated
    global leaveButtonScreen

    buttonActivated = False
    #on met en place le menu
    mainMenuScreen = UI.setup_main_menu()
    leaveButtonScreen = UI.setup_leave_button()
    buttonActivated = True
    #si on clique le la fonction clickedMenu s'execute
    mainScreen.onclick(clickedMenu)
    

#Fonction executé si on clique dans le menu
def clickedMenu(x, y):
    global mainMenuScreen
    global bgMenuScreen
    global buttonActivated

    if buttonActivated:

        verif_leave(x, y)
        #on test pour savoir si l'utilisateur clique sur un bouton
        if x >= -150 and x <= 150:
            if y <= 200 and y >= 75:
                #si les conditions sont respectees on lance la partie
                buttonActivated = False
                mainMenuScreen.clear()
                bgMenuScreen.clear()
                game()
                

            elif y <= 0 and y >= -125:
                #si les conditions sont verifiées, on affiches les règles
                mainMenuScreen.clear()
                rules()

            elif y <= -200 and y >= -325:
                mainMenuScreen.clear()
                options()
    
    
#Fonctions qui va etre executer lorsque le joueur clique sur l'ecran
def clickedGame(x, y):
    global secondCount
    global card
    global firstClick
    global buttonActivated
    global tDebut
    global drawing
    global warningScreen
    global drawingScreen
    global buttonsScreen
    global totalTime
    global difficulty

    if buttonActivated:
            
        #on recupere la joueur
        repPlayer = get_click(x, y)

        print(repPlayer)
        #Si la reponse vaut None, alors le joueur n'a pas cliqué sur un bouton, et on affiche alors le message d'avertissement
        if repPlayer == None:
            UI.display_warning(warningScreen)

        elif repPlayer == -1:
            pass
            
        #Sinon le joueur a bien cliqué sur un bouton et on continue le jeu
        else:
            #On clear bien les dessins de la manche precedente
            warningScreen.clear()
            drawingScreen.clear()

            #On verifie la reponse, si le joueur a juste on lui ajoute des points
            if check_rep(repPlayer, card):
                secondCount += difficulty[0]
                totalTime += difficulty[0]
                UI.display_rep(drawingScreen ,True)
                    
            #sinon on lui en enleve
            else:
                UI.display_rep(drawingScreen ,False)
                secondCount -= difficulty[1]
                totalTime -= difficulty[1]

            #on genere une carte
            card = generate_card()
            #puis on l'affiche
            buttonActivated = False
            UI.draw_card(card, drawings.turtleForms, drawings.turtleColors, drawingScreen, drawings.listCFD, drawings.listCSD)
            buttonActivated = True



#Fonction qui va afficher tout ce qu'il faut une fois la partie gagné
def win():
    global winScreen
    global buttonsScreen
    global timerScreen
    global buttonActivated
    global menuButtonScreen
    
    buttonActivated = False
    drawingScreen.clear()
    buttonsScreen.clear()
    timerScreen.clear()
    menuButtonScreen.clear()
    warningScreen.clear()
    winScreen = UI.win(totalTime)
    buttonActivated = True
    
    sc = winScreen.getscreen()
    sc.onclick(return_menu)

#Fonction qui va lancer une partie
def game():
    global displayWin
    global drawingScreen
    global card
    global bgScreen
    global scoreScreen
    global warningScreen
    global buttonsScreen
    global buttonActivated
    global totalTime
    global leaveButtonScreen
    global menuButtonScreen
    global continueC

    #autorise le timer a se decrementer
    continueC = True
    displayWin = True
    mainScreen.clear()
    #on met tout les affichage en place
    bgScreen, drawingScreen, warningScreen, buttonsScreen = UI.main_setup()
    leaveButtonScreen = UI.setup_leave_button()
    menuButtonScreen = UI.return_menu_button()
    #on genere la premier carte
    card = generate_card()
    #on lance le timer
    timer(count)
    #on met le nombre de seconde en place suivant le choix du joueur
    totalTime = count
    UI.draw_card(card, drawings.turtleForms, drawings.turtleColors, drawingScreen, drawings.listCFD, drawings.listCSD)
    buttonActivated = True
    #on defini le fait que lorsque que l'on clique, n execute la fonction 'clicked'
    mainScreen.onclick(clickedGame)
            


bgMenuScreen = UI.setup_bg_menu()

main_menu()
mainScreen.tracer(1000)
mainScreen.mainloop()
