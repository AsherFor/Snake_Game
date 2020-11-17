import turtle

#Draw Screen
sc = turtle.Screen()
sc.title("Snake Game")
sc.bgcolor('#FFFFFF')
sc.setup(width=1000, height=600)

snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("black")
snake_head.shapesize(stretch_wid=1, stretch_len=1)
snake_head.penup()
# snake_head.goto(0, 0)
snake_head.setpos(0, 0)

y = 0
x = 0
def up_move():
    y = snake_head.ycor()
    y += 20
    snake_head.sety(y)
    print(x, y)
    boundaries()


def down_move():
    y = snake_head.ycor()
    y -= 20
    snake_head.sety(y)
    print(x ,y)
    boundaries()


def left_move():
    x = snake_head.xcor()
    x -= 20
    snake_head.setx(x)
    print(x, y)
    boundaries()


def right_move():
    x = snake_head.xcor()
    x += 20
    snake_head.setx(x)
    print(x, y)
    boundaries()

def boundaries():
    if snake_head.xcor() >= 500 or snake_head.xcor() <= -500:
        print("end")
        sc.bye()
    if snake_head.ycor() >= 300 or snake_head.ycor() <= -300:
        print("endy")
        sc.bye()


# Keyboard bindings
sc.listen()
sc.onkeypress(up_move, "w")
sc.onkeypress(down_move, "s")
sc.onkeypress(left_move, "a")
sc.onkeypress(right_move, "d")

turtle.done()

