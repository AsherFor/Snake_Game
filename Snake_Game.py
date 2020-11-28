'''
Asher Forman
Snake Game
11/24/20
'''
import turtle
import random

Up = False
Down = False
Left = False
Right = False
stop_or_keep_playing = True
apple = turtle.Turtle()


#Draw Screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor('#00ff00')
width = 500
height = 500
window.setup(width= width, height= height)

# Snake head
snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("#FF00FF")
snake_head.penup()
snake_head.goto(0, 0)

# Make Apple
def spawn_apple():
    global apple
    apple.shape("circle")
    apple.color("#ff0000")
    apple.penup()
    apple.goto(0, 0)
    ran_x = random.randrange(-240, 240, 10)
    ran_y = random.randrange(-240, 240, 10)
    apple.setpos(ran_x, ran_y)



def check_boundaries(apple):
    global stop_or_keep_playing
    if snake_head.ycor() <= -245 or snake_head.ycor() >= 245:
        stop_or_keep_playing = False
        close_text()
    if snake_head.xcor() <= -245 or snake_head.xcor() >= 245:
        stop_or_keep_playing = False
        close_text()
    if ((apple.ycor() <= snake_head.ycor() + 12 and apple.ycor() >= snake_head.ycor() - 12) and
            (apple.xcor() <= snake_head.xcor() + 12 and apple.xcor() >= snake_head.xcor() - 12)):
            spawn_apple()




def close_text():
    close = turtle.Turtle()
    close.hideturtle()
    close.write("Wall hit", align="center", font=("Courier", 24, "normal"))

def head_up():
    global Up, Down, Left, Right
    Up = True
    Down = False
    Left = False
    Right = False

def head_down():
    global Up, Down, Left, Right
    Up = False
    Down = True
    Left = False
    Right = False

def head_left():
    global Up, Down, Left, Right
    Up = False
    Down = False
    Left = True
    Right = False

def head_right():
    global Up, Down, Left, Right
    Up = False
    Down = False
    Left = False
    Right = True

def close_game():
    exit()

def game_play():
    global Up, Down, Left, Right
    while stop_or_keep_playing == True:
        if Up == True:
            y = snake_head.ycor()
            y += 5
            snake_head.sety(y)

        if Down == True:
            y = snake_head.ycor()
            y -= 5
            snake_head.sety(y)

        if Left == True:
            x = snake_head.xcor()
            x -= 5
            snake_head.setx(x)

        if Right == True:
            x = snake_head.xcor()
            x += 5
            snake_head.setx(x)
        check_boundaries(apple)
        window.update()


# Keyboard bindings
window.listen()
window.onkeypress(head_up, "w")
window.onkeypress(head_down, "s")
window.onkeypress(head_left, "a")
window.onkeypress(head_right, "d")
window.onkeypress(close_game, "Escape")

spawn_apple()
game_play()
turtle.done()
