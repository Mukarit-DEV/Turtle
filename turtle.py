import turtle

tosh = turtle.Turtle()
tosh.color("red")
tosh.width(5)


def func1():
    tosh.forward(20)


def func2():
    tosh.left(45)


def func3():
    tosh.right(45)


def func4():
    sc.bye()

def func5():
    tosh.back(20)

def func6():
    tosh.penup()

def func7():
    tosh.pendown()


def main():
    global sc

    sc = turtle.Screen()
    sc.setup(700, 500)
    sc.title("Toshbaqa")
    sc.bgcolor("blue")

    sc.onkey(func1, "Up")
    sc.onkey(func2, "Left")
    sc.onkey(func3, "Right")
    sc.onkey(func4, "q")
    sc.onkey(func5, "Down")
    sc.onkey(func6, "u")
    sc.onkey(func7, "d")
    sc.listen()
    sc.mainloop()

main()
