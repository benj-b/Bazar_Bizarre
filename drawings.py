#Binome : Amiard Antoine / Benjamin Bernaud

import math as m
import turtle as t

#Fonction permettant de se deplacer sans écrire
def move_wo_draw(screen, x, y):
    screen.up()
    screen.goto(x,y)
    screen.down()

#Fonction qui dessine un polygone
def polygone(screen, cote, long):
    for loop in range(0, 4):
        screen.fd(long)
        screen.right(360/cote)

#Fonction qui dessine un soleil
def sun(screen, x, y, couleur):
    screen.up()
    screen.home()
    sc = screen.getscreen()
    sc.tracer(200)
    screen.speed(0)
    screen.ht()
    screen.fillcolor(couleur)
    star(c, x, y, "gold")
    screen.left(35)
    star(c, x-10, y, "gold")
    screen.up()
    screen.right(c.heading())
    screen.goto(x, y+17.5)
    screen.begin_fill()
    screen.circle(-34, 360)
    screen.end_fill()

#Fonction qui dessine une lune
def moon(screen, x, y, couleur, k):
    screen.up()
    screen.home()
    sc = screen.getscreen()
    sc.tracer(00)
    screen.pensize(2)
    screen.pencolor("gray")
    screen.fillcolor(couleur)
    screen.begin_fill()
    screen.left(180)
    move_wo_draw(screen, x, y+150)
    screen.circle(180*k, 182.5)
    screen.right(screen.heading()+180+42.5)
    screen.circle(-250*k, 92.5)
    screen.end_fill()


#Fonction qui dessine une fusée   
def rocket(screen,x, y, couleur,pensize=4,k=1):
    screen.up()
    screen.home()
    sc = screen.getscreen()
    sc.tracer(00)
    screen.pensize(pensize)
    screen.pencolor(couleur)
    move_wo_draw(screen, x, y)
    screen.left(135)
    screen.up()
    screen.circle(-200*k, 15)
    screen.down()
    screen.circle(-200*k, 5)
    BLW = screen.pos()
    screen.up()
    screen.circle(-200*k, 15)
    screen.down()
    TLW = screen.pos()
    screen.circle(-200*k, 55)
    screen.right(90)
    screen.circle(-200*k, 55)
    TRW = screen.pos()
    screen.up()
    screen.circle(-200*k, 15)
    BRW = screen.pos()
    screen.down()
    screen.circle(-200*k, 5)
    screen.right(screen.heading()+180)
    screen.fd((screen.xcor()-x)*2)
    screen.up()
    screen.goto(BLW)
    screen.down()
    screen.left(60)
    screen.fd(50*k)
    screen.right(90+40)
    screen.fd(70*k)
    screen.goto(TLW)
    screen.right(screen.heading())
    screen.up()
    screen.goto(BRW)
    screen.down()
    screen.right(60)
    screen.fd(50*k)
    screen.left(90+40)
    screen.fd(70*k)
    screen.goto(TRW)

    screen.pensize(2)
    screen.up()
    screen.goto(x+10*k, y+200*k)
    screen.down()
    screen.right(screen.heading()-90)
    screen.circle(10*k, 360)
    screen.up()
    screen.goto(x+20*k, y+200*k)
    screen.down()
    screen.circle(20*k, 360)
    screen.up()
    screen.goto(x+15*k, y+200*k)
    for loop in range(0, 6):
        screen.circle(15*k, 60)
        screen.dot(7*k)



#Fonction qui dessine une étoile  
def star(screen, x, y, couleur, taille = 75,k=1):
    sc = screen.getscreen()
    sc.tracer(200)
    screen.pensize(3)
    screen.pencolor(couleur)
    move_wo_draw(screen, x,y)
    screen.color(couleur)
    screen.begin_fill()
    screen.penup()
    screen.pendown()
    for loop in range(5):
        screen.forward(taille)
        screen.right(144)
        screen.forward(taille)
    screen.end_fill()



#Fonction qui dessine un flocon
def flake(screen, x, y, couleur,k=1):
    screen.up()
    screen.home()
    sc = screen.getscreen()
    sc.tracer(200)
    screen.pencolor(couleur)
    screen.pensize(3)
    move_wo_draw(screen ,x, y)
    screen.speed(0)
    screen.color(couleur)
    screen.hideturtle()
    screen.fillcolor(couleur)
    screen.begin_fill()
    for _ in range(0, 6):
        screen.right(180 - 360/6)
        screen.fd(40*k)
        screen.right(45)
        screen.fd(30*k)
        screen.left(90)
        screen.fd(10*k)
        screen.left(90)
        screen.fd((30 - (m.tan(m.radians(45))*10))*k)
        screen.right(135)
        screen.fd(30*k)
        screen.left(90)
        screen.fd(10*k)
        screen.left(90)
        screen.fd(30*k)
        screen.right(180 - 45)
        screen.fd((30 - (m.tan(m.radians(45))*10))*k)
        screen.left(90)
        screen.fd(10*k)
        screen.left(90)
        screen.fd(30*k)
        screen.right(45)
        screen.fd(40*k)
    screen.end_fill()
    screen.up()
    screen.home()

#Fonction qui dessine un satellite    
def satellite(screen, x, y, couleur,pensize=3, k=1):
    screen.up()
    screen.home()
    sc = screen.getscreen()
    sc.tracer(200)
    screen.pensize(pensize)
    screen.pencolor(couleur)
    screen.speed(0)
    screen.hideturtle()

    move_wo_draw(screen, x, y)


    for loop in range(2):
        screen.fd(75*k)
        screen.rt(90)
        screen.fd(100*k)
        screen.rt(90)

    move_wo_draw(screen, x,y-50*k)
    
    screen.rt(180)
    screen.fd(20*k)
    screen.rt(90)
    screen.fd(50*k)

    for loop in range(2):
        screen.lt(90)
        screen.fd(150*k)
        screen.lt(90)
        screen.fd(100*k)

    move_wo_draw(screen,x+75*k,y-50*k)
    
    screen.rt(90)
    screen.fd(20*k)
    screen.rt(90)
    screen.fd(50*k)
    for loop in range(2):
        screen.lt(90)
        screen.fd(150*k)
        screen.lt(90)
        screen.fd(100*k)

    move_wo_draw(screen, x+10*k, y-102*k)
    screen.lt(90)
    for loop in range(2):
        screen.fd(55*k)
        screen.rt(90)
        screen.fd(10*k)
        screen.rt(90)

    move_wo_draw(screen, x+20*k, y-115*k)

    for loop in range(2):
        screen.fd(35*k)
        screen.rt(90)
        screen.fd(7*k)
        screen.rt(90)

    move_wo_draw(screen, x+30*k, y-125*k)

    screen.rt(90)
    screen.circle(7.5*k,180)
    screen.lt(90)
    screen.fd(15*k)

    move_wo_draw(screen, x+30*k, y+2*k)

    screen.rt(180)
    for loop in range(2):
        screen.fd(15*k)
        screen.lt(90)
        screen.fd(5*k)
        screen.lt(90)

    move_wo_draw(screen, x+15*k, y+25*k)
    
    screen.rt(90)
    screen.circle(15*k,90)
    screen.fd(15*k)
    screen.circle(15*k,90)
    screen.lt(90)
    screen.fd(45*k)

    move_wo_draw(screen, x+37.5*k, y+31*k)
    
    screen.rt(90)
    screen.fd(10*k)

    move_wo_draw(screen, x+35*k,y+41*k)

    screen.begin_fill()
    screen.lt(180)
    screen.circle(5*k)
    screen.end_fill()

    screen.pensize(2)
    move_wo_draw(screen, x-160*k,y-2.5*k)
    
    i = 160
    for loop in range(15):
        screen.fd(95*k)

        move_wo_draw(screen, x-i*k, y-2.5*k)
        i -= 10

    move_wo_draw(screen, x+105*k,y-2.5*k)

    i = 105
    for loop in range(15):
        screen.fd(95*k)

        move_wo_draw(screen, x+i*k, y-2.5*k)
        i += 10

    screen.lt(90)
    
    i = 30
    for loop in range(5):
        move_wo_draw(screen, x+10*k,y-i*k)
        for loop in range(2):
            screen.fd(15*k)
            screen.circle(5*k,180)
            screen.fd(15*k)
            screen.circle(5*k,180)
        i += 15
        

    i = 30
    for loop in range(5):
        move_wo_draw(screen, x+50*k,y-i*k)
        for loop in range(2):
            screen.fd(15*k)
            screen.circle(5*k,180)
            screen.fd(15*k)
            screen.circle(5*k,180)
        i += 15


#Fonction qui dessine un satellite
def ovni(screen, x, y, couleur ,k=1):
    screen.up()
    screen.home()
    sc = screen.getscreen()
    sc.tracer(200)
    screen.pensize(3)
    screen.pencolor(couleur)
    move_wo_draw(screen, x ,y)
    screen.ht()
    screen.speed(10)
    screen.right(80/2)
    for loop in range(0, 2):
        screen.circle(180*k,26.67)
        posTemp = screen.pos()
        screen.right(90)
        screen.fd(20*k)
        screen.dot(10*k)
        screen.goto(posTemp)
        screen.left(90)
        
    screen.circle(180*k,26.67)
    screen.right(screen.heading()+ 180)
    screen.right(35)
    screen.circle(180*k, 25)
    screen.right(screen.heading()-90)
    screen.fd(20*k)
    screen.circle((87.44/2)*k, 180)
    screen.fd(20*k)
    screen.right(90)
    screen.left(135)
    posTemp = screen.pos()
    screen.circle(62*k, 90)
    screen.up()
    screen.goto(posTemp)
    screen.down()
    screen.left(screen.heading()+100)
    screen.circle(180*k, 25)
    screen.up()
    screen.goto(x+60*k,y-5*k)
    screen.dot(20*k)
    screen.goto(x+115*k,y-15*k)
    screen.dot(20*k)
    screen.goto(x+170*k, y-5*k)
    screen.dot(20*k)

#liste des formes et couleurs en language naturel
formes = ["étoile", "ovni", "satellite", "flocon", "fusée"]
couleurs = ["jaune", "vert", "gris", "bleu", "rouge"]
#liste des fonctions qui dessine les formes et liste des noms de couleurs pour turtle
turtleForms = [star, ovni, satellite, flake, rocket]
turtleColors = ["yellow", "Lime", "dark gray", "dodger blue", "red"]
#liste des fututes emplacement des dessins sur le 'plateau de jeu' 
listCFD = [(-150, 30), (-300, 0), (-275, 50), (-175, -5), (-150, -120)]
listCSD = [(120, 30), (50, 0), (250, 50), (150, -5), (125, -125)]

