from random import *
print("Welcome to the TWICE quiz!!")
print("Answer questions correctly to get points. Your score will be shown at the end")
score = 0

with open ('questions.txt' , 'r') as file:
    lines = file.readlines()
    questions = [line.strip() for line in lines if line.strip()][:10]

random_line_number = randint(0, len(questions) - 1)
random_question = questions[random_line_number].strip()
print(f"Question: {random_question}")

with open("answers.txt", "r") as file:
    questions = file.readlines()

answer = input()
if answer+"\n" in questions:
    print("that's correct!!")
    score += 1
elif answer+"\n" not in questions:
    print("sorry, wrong answer..")
else:
    with open ("questions.txt" , 'r') as file:
        questions = file.readlines()

print(f"your total score is: {score}") 