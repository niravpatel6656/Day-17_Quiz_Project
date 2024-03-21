# Importing the Question class from question_model module
from question_model import Question

# Initializing the question number
question_number = 0

# Class to manage the quiz
class QuizBrain():
    def __init__(self, q_list):
        # Initializing instance variables
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # Method to check if there are remaining questions
    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    # Method to present the next question
    def next_question(self):
        # Getting the current question from the question list
        current_question = self.question_list[self.question_number]

        # Prompting user for the answer to the current question
        user_answer = input(f"{current_question.text} - Enter your answer: ")

        # Checking if the answer is correct
        if user_answer.lower() == current_question.answer.lower():
            # If correct, updating score and providing feedback
            print("Correct!")
            self.score += 1
            print(f"Your score is {self.score}")
        else:
            # If incorrect, providing correct answer and score
            print("Wrong answer.")
            print(f"The correct answer is {current_question.answer}.")
            print(f"Your score is {self.score}")

