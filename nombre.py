import turtle
tortugajuan = turtle.Turtle()

colors=['orange', 'red', 'yellow', 'blue', 'red', 'orange', 'light green','light blue',]

tortugajuan.pensize(15)
#Letra J
tortugajuan.pencolor("red")
tortugajuan.goto(120,0)
tortugajuan.goto(80,0)
tortugajuan.goto(80,-100)
tortugajuan.goto(-50,-50)
tortugajuan.penup()
#Letra U
tortugajuan.goto(120,-25)
tortugajuan.pendown()
tortugajuan.pencolor("black")
tortugajuan.goto(120,-50)
tortugajuan.goto(120,-100)
tortugajuan.goto(170,-100)
tortugajuan.goto(170,0)
tortugajuan.penup()
#Letra A
tortugajuan.goto(210,-0)
tortugajuan.pendown()
tortugajuan.pencolor("orange")
tortugajuan.goto(190,-100)
tortugajuan.penup()
tortugajuan.goto(210,0)
tortugajuan.pendown()
tortugajuan.goto(250,-100)
tortugajuan.penup()
tortugajuan.goto(190,-70)
tortugajuan.pendown()
tortugajuan.goto(250,-70)
tortugajuan.penup()
tortugajuan.goto(270,0)
#Letra N
tortugajuan.pendown()
tortugajuan.pencolor("light green")
tortugajuan.goto(270,-100)
tortugajuan.goto(270,0)
tortugajuan.goto(320,-100)
tortugajuan.goto(320,0)
tortugajuan.penup()
tortugajuan.goto(340,0)
#Letra M (al revés)
tortugajuan.pendown()
tortugajuan.pencolor("brown")
tortugajuan.goto(370,-100)
tortugajuan.goto(390,0)
tortugajuan.goto(420,-100)
tortugajuan.goto(440,0)
tortugajuan.penup()
tortugajuan.goto(440,0)

#Linea de colores xd
for i in range(20):
  tortugajuan.goto(-50,-130)
  tortugajuan.hideturtle
  tortugajuan.pendown()
  tortugajuan.color(colors[i%8])
  tortugajuan.forward (500)
  tortugajuan.left(90)
  tortugajuan.right(90)
  tortugajuan.speed(100)
tortugajuan.penup()
tortugajuan.goto(165,120)
tortugajuan.pendown()
tortugajuan.pensize(4)

