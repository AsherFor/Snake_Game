'''
Asher Forman
Snake Game
11/24/20
'''
import turtle
import random

stop_or_keep_playing = True
apple = turtle.Turtle()


# Draw Screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor('#00ff00')
width = 500
height = 500
window.setup(width= width, height= height)

# Snake head
snake_head = turtle.Turtle()
snake_head.direction = "stop"
snake_head.shape("square")
snake_head.color("#FF00FF")
snake_head.penup()
snake_head.goto(0, 0)

# Snake Body
snake_body = []


# Make Apple
def spawn_apple():
    global apple
    apple.shape("circle")
    apple.color("#ff0000")
    apple.penup()
    apple.speed(0)
    ran_x = random.randrange(-240, 240, 5)
    ran_y = random.randrange(-240, 240, 5)
    apple.setpos(ran_x, ran_y)


def spawn_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("#FF00FF")
    new_segment.penup()
    snake_body.append(new_segment)


def check_boundaries(apple):
    global stop_or_keep_playing
    if snake_head.ycor() <= -245 or snake_head.ycor() >= 245:
        stop_or_keep_playing = False
        close_text()
    if snake_head.xcor() <= -245 or snake_head.xcor() >= 245:
        stop_or_keep_playing = False
        close_text()
    if (snake_head.distance(apple)) <= 20:
        spawn_apple()
        spawn_segment()




def close_text():
    close = turtle.Turtle()
    close.hideturtle()
    close.write("Wall hit", align="center", font=("Courier", 24, "normal"))

def head_up():
    snake_head.direction = "up"

def head_down():
    snake_head.direction = "down"

def head_left():
    snake_head.direction = "left"

def head_right():
    snake_head.direction = "right"

def close_game():
    turtle.bye()

def game_play():
    while stop_or_keep_playing == True:
        if snake_head.direction == "up":
            y = snake_head.ycor()
            y += 20
            snake_head.sety(y)

        if snake_head.direction == "down":
            y = snake_head.ycor()
            y -= 20
            snake_head.sety(y)

        if snake_head.direction == "left":
            x = snake_head.xcor()
            x -= 20
            snake_head.setx(x)

        if snake_head.direction == "right":
            x = snake_head.xcor()
            x += 20
            snake_head.setx(x)
        check_boundaries(apple)
        window.update()
        # Move the end segment snake_body
        for index in range(len(snake_body)-1, 0, -1):
           x = snake_body[index -1].xcor()
           y = snake_body[index -1].ycor()
           snake_body[index].goto(x, y)
        if len(snake_body) > 0:
            x = snake_head.xcor()
            y = snake_head.ycor()
            snake_body[0].goto(x, y)

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