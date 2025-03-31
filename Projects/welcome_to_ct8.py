###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("spring")
mySprite = codesters.Sprite("catimage")
mySprite.set_size(0.25)
mySprite.say("Helllo!!!!!")
mySprite = codesters.Sprite("baseball",-200,200)


print("\n\nWhen you have found the CARDINAL, click here, then use CTRL C to end the program\n\n")