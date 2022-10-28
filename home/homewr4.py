import turtle

tt = turtle.Turtle()
turtle.bgcolor("gold")
tt.pencolor("red")
tt.speed(0)
tt.penup()
tt.goto(1, 250)
tt.pendown()

forDis = 0
dR = 0

while (True):
    tt.forward(forDis)
    tt.right(dR)
    forDis += 3

    dR += 1
    if dR == 250:
        break

    tt.hideturtle()

turtle.done()
