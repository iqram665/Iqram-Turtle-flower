import turtle

#window setup
s = turtle.Screen()
s.setup(width=750, height=750)
s.bgcolor("black")
s.title("iqram python Turtle Flower design")

t = turtle.Turtle()
t.speed(0)
t.width(2)

#color list
colors = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "INDIGO", "VIOLET", "PINK", "MAGENTA", "CYAN", "BLUE", "LIME", "MAROON", "NAVY", "OLIVE", "TEAL", "GRAY", "SILVER"]

# Drawing loop
for i in range(155):
    t.pencolor(colors[i % len(colors)])
    t.circle(100)
    t.left(20)
t.hideturtle()
turtle.done()   
