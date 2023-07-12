from data import question_data

from quiz import Quiz
class Question:
    def __init__(self, question, answer, id):
        self.question = question
        self.answer = answer
        self.id = id

def create_question_bank(data):
    i = 1
    question_bank = []
    for question in data:
        text = question["text"]
        answer = question["answer"]
        q = Question(text, answer, i)
        question_bank.append(q)
        i += 1

    return question_bank

bank = create_question_bank(question_data)
new_quiz = Quiz(bank)
new_quiz.quiz()

