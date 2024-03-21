from question_model import Question
# from main import question_bank
#TODO 1. Asking the question

question_number = 0

class QuizBrain():
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # TODO 3. Checking if we are at the end of the quiz
    def still_has_questions(self):
        return len(self.question_list) > self.question_number
    def nextquestion(self):
        current_question = self.question_list[self.question_number]

        user_answer = input(f"{current_question.text} - Enter the answer")
        # TODO 2. Checking if the answer was correct
        if user_answer.lower() == current_question.answer.lower():
            print("yeeeeeee")
            self.score += 1
            print(f"your score is {self.score}")
        else:
            print("wrong answer\n")
            print(f"correct answer is {current_question.answer}\n")
            print(f"your score is {self.score}\n")



