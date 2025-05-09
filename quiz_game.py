# For Assignment 10: Quiz
# Create the Quiz program that read the output file of the Quiz Creator.
# The user will answer the randomly selected question and check if the answer is correct
# ////=======================================================================================///

# INITIALIZE the QUIZ Game

# DISPLAY the welcome message to the players
print("🧐 Welcome to this short Math Quiz Game! Let's test your problem solving skills!")

# ASK the user to inpute filename of quiz (its default is set to "created_quiz_questions.txt")
filename = input("Enter the filename of the quiz (press Enter to user 'created_quiz_questions.txt'): ")
if filename.strip() == "":
    filename = "created_quiz_questions.txt"

# CALL function to load up the questions form the created text file
#      OPEN file in read mode
#      READ all lines
#      INITIALIZE an empty list to store each question set
#      FOR each line group (question + choices + correct answer)
#           break down the text and extract:
#             Question, Choices (a, b , c, d), Correct Answer
#           ADD each question set to the list
#      RETURN list of break downed txt questions

import random

def load_questions_from_file(filename):
    questions = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line == "":
                i += 1
                continue
            question = line
            choices = {}
            for choice_number in range (1, 5):
                key, value = lines[i + choice_number].strip().split(": ")
                choices[key] = value
            correct_answer_line = lines[i + 5].strip()
            correct_answer = correct_answer_line.split(": ")[1]
            questions.append({"question": question, "choices": choices, "answer": correct_answer})
            i += 7
    except FileNotFoundError:
        print(" ⚠️CAUTION⚠️ Cannot locate the file. Please type in an existing filename and check if it is correct.")
        return []
    return questions

# IF no questions were found
#   DISPLAY an error message
#   END program

quiz_data = load_questions_from_file(filename)
if not quiz_data:
    print("No questions were found. Exiting the quiz game.")
    exit()

# SHUFFLE the list of questions (so that the user will answer the questions in a randomized way)
random.shuffle(quiz_data)

# SET score to 0
# SET total to number of questions

# FOR each questions in the list
#       DISPLAY questions and choices (a to d)  
#       ASK user for their answer (a, b, c, or d)
#       IF user's answer is equal to the correct answer
#           DISPLAY "Correct Answer!" message text
#           INCREMENT score 
#       ELSE    
#           DISPLAY "Incorrect Answer." message text

# after all of the questions were displayed
#       DISPLAY final score out of how many questions were provided

# DISPLPAY a thank you message in the end

# END the Quiz Game