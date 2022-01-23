import turtle
wn=turtle.Screen()
george=turtle.Turtle()
wn.exitonclick()

sides=6


for x in range(360):
                #
               
                george.forward(x*3/sides+x)
                george.left(360/sides+1)
 
