print("Welcome to my computer quiz! ")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay, let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower == "central processing unit":
    print("Well done")
    score += 1
else:
    print("Please try again. ")

answer = input("What does GPU stand for? ")
if answer.lower == "graphic processing unit":
    print("Well done")
    score += 1
else:
    print("Please try again. ")

answer = input("What does RAM stand for? ")
if answer.lower == "random access memory":
    print("Well done")
    score += 1
else:
    print("Please try again. ")

print("You've got " + str(score) + "questions correct! ")