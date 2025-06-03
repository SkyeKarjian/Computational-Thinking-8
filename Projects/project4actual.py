# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite


# Section 2 - Variables
# TODO - add starting values for all the variables
x1 = -250
y1 = 200
x2 = -250
y2 = 50
x3 = -250
y3 = -80
x4 = -250
y4 = -210
# Section 3 - Setup
set_background("castle")
t1 = create_sprite("madelyn",x1,y1)
t2 = create_sprite("cat",x2,y2)
t3 = create_sprite("madelyn (2)",x3,y3)
t4 = create_sprite("bunny",x4,y4)


# # Section 4 - Racing
for i in range(30):
	x1 += random.randint(1, 6)
	x2 += random.randint(2, 6)
	x3 += random.randint(1, 4) #slowest is madelyn 2
	x4 += random.randint(3, 6) #fastest is the bunny
	t1.goto(x1, y1)
	t2.goto(x2, y2)
	t3.goto(x3, y3)
	t4.goto(x4, y4)
	time.sleep(0.1)


# # Section 5 - Winner
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("player 2 wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("player 3 wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    print("player 4 wins!")




turtle.exitonclick()
