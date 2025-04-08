#Start
import turtle
t = turtle.Turtle()

t.speed( 10 )
t.goto(0, 0)


colors = ["pink", "purple", "blue"]
for i in range (800):
    t.color( colors [ i % 3])
    t.forward( 70 + i)
    t.left (290)




turtle.exitonclick()