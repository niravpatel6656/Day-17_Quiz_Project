from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quizbrain = QuizBrain(question_bank)
score = 0
while quizbrain.still_has_questions():
    quizbrain.nextquestion()
    quizbrain.question_number += 1




