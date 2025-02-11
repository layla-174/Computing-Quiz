from random import *
print("Welcome to the TWICE quiz!!")
print("Answer questions correctly to get points. Your score will be shown at the end")
score = 0

with open ('questions.txt' , 'r') as file:
    questions = file.readlines()

random_line_number = randint(0, len(questions) - 1)
random_question = questions[random_line_number].strip()
print(f"Question: {random_question}")

with open("answers.txt", "r") as file:
    i = 0
    answers = file.readlines()
    for answer in answers:
        print(questions[i])
        userInput = input()
        if answer == userInput+"\n":
            print("that's correct!!")
            score += 1
        else:
            print("sorry, wrong answer..")
        i += 1

print(f"your total score is: {score} !!") 