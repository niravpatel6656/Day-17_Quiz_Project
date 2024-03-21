# Importing necessary classes and data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Creating an empty list to store Question objects
question_bank = []

# Iterating through the question data
for question in question_data:
    # Extracting question text and answer from each dictionary in the data
    question_text = question["text"]
    question_answer = question["answer"]
    # Creating a new Question object with the extracted text and answer
    new_question = Question(question_text, question_answer)
    # Appending the new Question object to the question bank
    question_bank.append(new_question)

# Creating a QuizBrain object with the question bank
quizbrain = QuizBrain(question_bank)

# Initializing score
score = 0

# Looping until there are no more questions in the quiz
while quizbrain.still_has_questions():
    # Displaying the next question
    quizbrain.next_question()
    # Incrementing question number
    quizbrain.question_number += 1
