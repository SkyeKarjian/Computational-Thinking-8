###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("winter")
q1 = codesters.Square( 100, 100, 200, 'blue')
q2 = codesters.Square( -100, 100, 200, 'yellow')
q3 = codesters.Square( -100, -100, 200, 'red')
q4 = codesters.Square( 100, -100, 200, 'green')


s1 = codesters.Sprite("outer banks.jpg", 100, 100)
s1.set_size(0.35)
s2 = codesters.Sprite("sabrina.webp", -100, -100)
s2.set_size(0.3)
s3 = codesters.Sprite("pets.jpg", 100, -100)
s3.set_size(0.2)
s4 = codesters.Sprite("madelyn.jpg", -100, 100)
s4.set_size(0.2)


message1 = codesters.Text("Skye Karjian",0,220,"red")
message2 = codesters.Text("Madelyn Cline is the meaning of life.",0,-220,"black")