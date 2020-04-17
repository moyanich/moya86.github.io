# Working with strings

string_exp = "Tomato"
print(string_exp)

# Printing an index
exp_2 = "Dance Moms"
print(exp_2[2])
print("apple"[4])

# String Slicing
exp_3 = "Tomato"

# Slicing a string from the beginning to an end point
print(exp_3[:3])

# Slicing a string from a starting point to an end point
print(exp_3[2:5])

# Slicing a string from a starting point to the end of string
print(exp_3[2:])


# STRING CONCATENATION
# Using the plus(+) operator
print("Good" + " " + "morning")

concatenated_string = "evening prim" + "-" + "rose"
print(concatenated_string)
print(concatenated_string[4])
print(concatenated_string[1:4])


example = "Just do it!"
print(example[10])
print(example[5:7])
print(example[8:])
print(example[:4])
print(example[5:7] + " " + example[8:])
print("Don't" + " " + example[5:7] + " " + example[8:])

# Refactored Code

sentence = "Just do it!"

sentence_slided = sentence[10]
print(sentence_slided)

sentence_slided_2 = sentence[5:7]
print(sentence_slided_2)

sentence_slided_3 = sentence[8:]
print(sentence_slided_3)

sentence_slided_4 = sentence[:4]
print(sentence_slided_4)

print("Don't" + " " + sentence_slided_2 + " " + sentence_slided_3)

# STRING METHODS
# isupper() and islower()


