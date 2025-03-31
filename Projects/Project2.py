#Beginning: create celebrity point variables
olivia_rodrigo_points = 0
sabrina_carpenter_points = 0

#Middle: Ask my questions 
answer = input ("Do you have A) Dark hair, or B) Light hair?")
if answer == "A":
    olivia_rodrigo_points += 1
elif answer == "B":
    sabrina_carpenter_points += 1


answer = input ("Do you like A) the color purple or B) the color blue?")
if answer == "A":
    olivia_rodrigo_points += 1
elif answer == "B":
    sabrina_carpenter_points += 1


answer = input ("Which movie do you like better A) Tall Girl, or B) High School Musical?")
if answer == "A":
    sabrina_carpenter_points += 1
elif answer == "B":
    olivia_rodrigo_points += 1


answer = input ("Would you rather A) play guitar or B) do your skincare?")
if answer == "A":
    olivia_rodrigo_points += 1
elif answer == "B":
    sabrina_carpenter_points += 1


answer = input ("Do you like A) skirts, or B) dresses?")
if answer == "A":
    olivia_rodrigo_points += 1
elif answer == "B": 
    sabrina_carpenter_points += 1

#End: Results
if olivia_rodrigo_points > sabrina_carpenter_points:
    print("You are more like Olivia Rodrigo!")
if sabrina_carpenter_points > olivia_rodrigo_points:
    print("You are more like Sabrina Carpenter!")