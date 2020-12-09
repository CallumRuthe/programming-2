# Math Quiz

import sys
import time
from pygame import mixer


# set up the sound effect for self destruct
mixer.init()
mixer.music.load("./sounds/Explosion_Sound_Effect.mp3")


# Create variables
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
    "question_5": "pythagoras of samos",
}


# Go through the introduction
# Introduce the user to the quiz
print("Hello! My name is M4th Tut0r.\nMy job is to test your mathematical ability.\n")

# Find out if the user is ready to begin
user_ready = input("Are you ready to begin the quiz: ").strip("!,.? ")

# If the user is not ready to start, power down; if they are ready, continue to questions; otherwise self destruct
if user_ready.lower() == "no":
    print("\nPowering Down")
    sys.exit()
elif user_ready.lower() == "yes":
    print("\nPerfect. We will now begin the quiz!\n")
else:
    print("\nUncompilable. Self destruct sequence initiating.")
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
    print("Goodbye user")
    mixer.music.play()
    time.sleep(3)
    sys.exit()


# Go through the questions
# Keep track of what question we are on
question_number = 0

# For each question
for q in questions:
    # Ask a question and get the user response
    question_number += 1
    print(f"Question {question_number}: ")
    print(q)
    response = input("A: ").lower().strip(".?, !")

    answer = answers[f"question_{question_number}"]
    # Inform the user if they got the question right or wrong
    # If they got the question right, add to their score
    # Give feedback based on how they did on the question
    if response == answer:
        print("That's correct. Good Job!\n")
        correct_answers += 1
    else:
        print(f"Unfortunately that is not correct. The correct answer was: {answer} \nBetter luck with the next question.\n")


# Congratulate the user based on how they did and tell them how many questions they got correct
if correct_answers < 3:
    print(f"You might want to study some more. You have completed the quiz with {correct_answers}/5 questions correct. That's {100 * correct_answers / 5}%")
elif correct_answers < 5:
    print(f"Well done! You have completed the quiz with {correct_answers}/5 questions correct. That's {100 * correct_answers / 5}%")
else:
    print(f"Amazing, you got everything correct! You have completed the quiz with {correct_answers}/5 questions correct. That's {100 * correct_answers / 5}%")