from turtle import Turtle, Screen
import time
import random


# počítání score
score = 0
highest_score = 0
# nastavení okna
screen = Screen()
screen.bgcolor("gainsboro")
screen.title("Vítejte ve hře Snake.")
# velikost okna
screen.setup(width=500, height=500)
# vypnutí refreshování okna
screen.tracer(False)

# hadí hlava
head = Turtle("circle")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
# počátecní pohyb (stop nic nedělá)
head.direction = "stop"

# potrava pro hada
mouse = Turtle("circle")
mouse.color("green")
mouse.penup()
mouse.goto(100, 100)

# popisek score
score_text = Turtle("square")
score_text.speed(0)
score_text.color("black")
score_text.penup()
score_text.hideturtle()
score_text.goto(0, 225)
score_text.write("Skóre: 0  Nejvýšší scóre: 0", align="center", font=("Arial", 16))


# tělo hada
body_parts = []


# funkce pohybu
def move():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y + 20)

  if head.direction == "down":
    y = head.ycor()
    head.sety(y -20)

  if head.direction == "right":
    x = head.xcor()
    head.setx(x + 20)

  if head.direction == "left":
    x = head.xcor()
    head.setx(x - 20)

# funkce směru pohybu
def move_up():
  if head.direction !=  "down":
     head.direction = "up"

def move_down():
  if head.direction !=  "up":
     head.direction = "down"

def move_right():
  if head.direction !=  "left":
     head.direction = "right"

def move_left():
  if head.direction !=  "right":
     head.direction = "left"

  # ovládání hada  klávesy
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_left, "a")


# hlavní cyklus
while True:
  screen.update()


   # kolize hada s okrajem okna
  if head.xcor() > 240 or head.xcor() < -240 or head.ycor() > 240 or head.ycor() < -240:
    time.sleep(2)
    head.goto(0,0)
    head.direction = "stop"
    

    # skrytí částí těla mimo obrazovku
    for body_part in body_parts:
        body_part.goto(1000, 1000)

    # odstranění listu s částmi těla
    body_parts.clear()
    # reset score
    score = 0
    # vyčistění score
    score_text.clear()
    # vypsání score
    score_text.write(f"Skóre: {score}  Nejvýšší scóre: {highest_score}",
                      align="center", font=("Arial", 16))


  # podmínka kolize objektů had sní myš
  if head.distance(mouse) < 20:
    x = random.randint(-230, 230)
    y = random.randint(-230, 230)
    mouse.goto(x, y)
    

    # přidání části těla po kolizi objektů
    new_body_part = Turtle("circle")
    new_body_part.speed(0)
    new_body_part.color("orange")
    new_body_part.penup()
    body_parts.append(new_body_part)

    # zvýšení score
    score += 10
    # podmínka pro nejvyšší score
    if score > highest_score:
      highest_score = score
    # vyčištění starého textu
    score_text.clear()
    # vypsání score
    score_text.write(f"Skóre: {score}  Nejvýšší scóre: {highest_score}",
                      align="center", font=("Arial", 16))

  #  přidání části těla na konec těla
  for index in range(len(body_parts) - 1, 0, -1):
    x = body_parts[index - 1].xcor()
    y = body_parts[index - 1].ycor()
    body_parts[index].goto(x, y)

 
  # přidání první části těla za hlavu 
  if len(body_parts) > 0:
    x = head.xcor()
    y = head.ycor()
    body_parts[0].goto(x,y)
  
  move()

  # kolize hlavy s tělem
  for one_body_part in body_parts:
    if one_body_part.distance(head) < 20:
      time.sleep(2)
      head.goto(0, 0)
      head.direction = "stop"
      
       # skrytí částí těla mimo obrazovku
      for body_part in body_parts:
          body_part.goto(1000, 1000)

      # odstranění listu s částmi těla
      body_parts.clear()
      # reset score
      score = 0
      # vyčištění textu score
      score_text.clear()
      # vypsání score
      score_text.write(f"Skóre: {score}  Nejvýšší scóre: {highest_score}",
                      align="center", font=("Arial", 16))

  time.sleep(0.15)
  

screen.exitonclick()
