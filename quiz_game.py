# For Assignment 10: Quiz
# Create the Quiz program that read the output file of the Quiz Creator.
# The user will answer the randomly selected question and check if the answer is correct
# ////=======================================================================================///

# INITIALIZE the QUIZ Game


# DISPLAY the welcome message to the players


# ASK the user to inpute filename of quiz (its default is set to "created_quiz_questions.txt")


# CALL function to load up the questions form the created text file
#      OPEN file in read mode
#      READ all lines
#      INITIALIZE an empoty list to store each question set
#      FOR each line group (question + choices + correct answer)
#           break down the text and extract:
#             Question, Choices (a, b , c, d), Correct Answer
#           ADD each question set to the list
#      RETURN list of break downed txt questions

# IF no questions were found
#   DISPLAY an error message
#   END program

# SHUFFLE the list of questions (so that the user will answer the questions in a randomized way)

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