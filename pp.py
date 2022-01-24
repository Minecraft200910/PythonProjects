import turtle
t=turtle.Pen()

sides=6
colors=["red","yello","blue","orange","green","purple"]
for x in range(360):
    t.pencolor(colors[x])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)
