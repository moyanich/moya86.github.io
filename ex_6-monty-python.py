# Programming Challenge: Monty Python
# In a .py file, create a program and use input() three times to get answers to the following
# questions from a user.  Store each of the answers in a variable.
# What is your name?
# What is your quest?
# What is your favorite color?
# Then, concatenate everything into a string within a print() statement with
# the form "So your name is [name], your quest is [quest], and your favorite color is [color]."

answers = []

name = str(input("What is your name? "))
answers.append(name)
quest = str(input("What is your quest? "))
answers.append(quest)
color = str(input("What is your favorite color? "))
answers.append(color)

print(answers)
print("So your name is " + answers[0] + " your quest is " + answers[1] + " and your favorite color is " + answers[2] + " .")