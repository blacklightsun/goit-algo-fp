import turtle
# треба розгорнути поле малювання черепашки на максимум

def pythagoras_tree(t, order, size):
    if order == 0:
        t.color("green")
        t.forward(size)
        t.left(180)
        t.forward(size)
        t.color("brown")

    else:
        t.color("brown")
        t.forward(size)
        t.left(45)
        pythagoras_tree(t, order - 1, size / 1.5)
        t.left(90)
        pythagoras_tree(t, order - 1, size / 1.5)
        t.left(45)
        t.forward(size)


def draw_pythagoras_tree(order, size=200):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(3)
    t.penup()
    t.left(90)
    t.goto(0, -300)
    t.pendown()

    pythagoras_tree(t, order, size)

    window.mainloop()


# Виклик функції
draw_pythagoras_tree(int(input('Введіть рівень рекурсії (ціле число від 1 до безкінечності)-> ')))