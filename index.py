# Assignment 5 Program 3: Life stages
#
# Create a program that ask for an age of a person
# Display the life stage of the person.
# Rules:
# 0 - 12 : Kid
# 13 - 17 : Teen
# 18 : Debut
# 19 above : Adult

input_Age = int(input("Enter your Age: "))

if input_Age >= 0 and input_Age < 13:
    print("Age: " + str(input_Age) +"\nStage of Life: Kid")
elif input_Age >= 13 and input_Age < 18:
    print("Age: " + str(input_Age) +"\nStage of Life: Teen")
elif input_Age == 18:
    print("Age: " + str(input_Age) +"\nStage of Life: Debut")
elif input_Age >= 19:
    print("Age: " + str(input_Age) +"\nStage of Life: Adult")