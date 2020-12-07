# Math Quiz

import sys

# Create a counter to keep track of score
correct_answers = 0

# Create variable for each question
question_one = "What is: 7 + 4 \n"
question_two = "What is the 11th prime number \n"
question_three = "What is: (31 + 14) * 3 / 5 \n"
question_four = "Which of the following numbers are Mersenne Prime's: \na) 8191 \nb) 31 \nc) a and b \nd) 2048 \n"
question_five = "What is the full name of the person which the pythagorean theorem is named after? \n"

questions = [question_one, question_two, question_three, question_four, question_five]

# Create a dictionary containing the answer to each question
answers = {
    "question_1": "11",
    "question_2": "31",
    "question_3": "27",
    "question_4": "c",
    "question_5": "Pythagoras of Samos",
}

# Introduce the user to the quiz
print("Hello! My name is M4th Tut0r.\nMy job is to test your mathematical ability.\n")

# Find out if the user is ready to begin
user_ready = input("Are you ready to begin the quiz: ")

# If the user is not ready to start, power down. Otherwise continue to the quiz.
if user_ready.lower() == "no":
    print("\nPowering Down")
    sys.exit()
elif user_ready.lower() == "yes":
    print("\nPerfect. We will now begin the quiz!\n")
else:
    print("\nIncomputable. Self destruct sequence initiating.")
    for i in range(10, 0, -1):
        print(i)
    print("Goodbye user")
    sys.exit()


question_number = 0

# For each question
for q in questions:
    # Ask a question and get the user response
    question_number += 1
    print(f"Question {question_number}: ")
    print(q,"\n")
    response = input("A:")
    print("\n")

    answer = answers[f"question_{question_number}"]
    # Inform the user if they got the question right or wrong
    # If they got the question right, add to their score
    # Give feedback based on how they did on the question
    if response == answer:
        print("That's correct. Good Job!\n")
        correct_answers += 1
    else:
        print(f"Unfortunately that is not correct. The correct answer was: {answer} \nBetter luck with the next question.\n")

# Congratulate the user and tell them how many questionts they got correct
print(f"Congratulations! You have completed the quiz with {correct_answers}/5 questions correct.")