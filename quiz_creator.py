# Assignment 9: Quiz Creator
# Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. Write the collected data to a text file. Ask another question until the user chose to exit.
# Hint: 
# On the next assignment, you will create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.
# Format the data written on the text file so it is easier the read on the next assignment.
# Feel free to use any library


# All of the questions, choices, and the correct answer shall be saved to a separate file (.txt)
     # Define a function save_to_file()
        # A text file will open in appen mode.
        # Write the question.
        # Write each option with its respective label (a, b, c, d).
        # Write the correct answer.
        # Format the txt file by adding a space between entries for better readability to the user.
def save_to_file(question, choices, correct_answer, filename="created_quiz_questions.txt"):
    with open(filename, "a") as file:
        file.write(question + "\n")
        for choice, answer in choices.items():
            file.write(choice + ": " + answer + "\n")
        file.write("Correct Answer: " + correct_answer + "\n\n")

# Make a welcome message to the user.
def main():
    print("Hello User, welcome to this Quiz Creator!")

# Create the loop in able for the user to input as many quiz questions that they want.
    # Asking the user to input a quiz question and then store it.
    while True:
        question = input("Enter the question: ")

    # Make a dictionary where it stores the 4 possible answers (a, b, c, d).
        # For each letter chocies (a, b, c, d), the user will enter the answer and store it to the dictionary.
        choices = {}
        for choice in ['a', 'b', 'c', 'd']:
            answer = input("Enter the answer for " + choice + ": ")
            choices[choice] = answer

    # Asking the user to input the correct answer that is found in one of the following letter choices: (a, b, c, d)
        # For consistency, the letter input should be lowercased, we will be converting them.
        correct_answer = input("Enter the correct answer (a, b, c, or d): ").lower()

    # Make a visual display feedback for the questions entered (for more convenience visually in letting the user know what answer options are correct or not)
        # Make a loop for each answer option
        # If the option is the correct answer, print it with a green square emoji text (🟩).
        # If the option is not the correct answer, print it with a red square emoji text (🟥).
        print("Question feedback:")
        for choice, answer in choices.items():
            if choice == correct_answer:
                print(choice + ": " + answer + " 🟩")
            else:
                print(choice + ": " + answer + " 🟥")

    # Ask the user if they want to put in another question.
        # If the response is "yes" then the loop continues, if "no" then the loop breaks

# If the user wants to exit the program, put in a thank message to the user 