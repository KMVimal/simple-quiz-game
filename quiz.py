print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("LETS START!")
score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("incorrect!")
    print("Correct answer: central processing unit")

answer = input("What does gpu stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("incorrect!")
    print("Correct answer: graphics processing unit")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("incorrect!")
    print("Correct answer: random access memory")

answer = input("What does HDD stands for? ")
if answer.lower() == "hard disk drive":
    print("Correct!")
    score += 1
else:
    print("incorrect!")
    print("Correct answer: hard disk drive")

answer = input("What does SSD stands for? ")
if answer.lower() == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("incorrect!")
    print("Correct answer: solid state drive")

print("congratulations!")
print("You got " + str(score) + "questions correct")
print("you got " + str((score / 5) * 100))
