from random import *
print("Welcome to the TWICE quiz!!")
print("Answer questions correctly to get points. Your score will be shown at the end")


with open ('questions.txt' , 'r') as file:
    questions = file.readlines()

random_line_number = randint(0, len(questions) - 1)
random_question = questions[random_line_number].strip()
print(f"Question: {random_question}")


with open("answers.txt", "r") as file:
    questions = file.readlines()

answer = input()
if answer+"\n" in questions:
    print("Correct")
else:
    print("Sorry, wrong answer")