from question_model import Question
from data import question_data
from quiz_brain import Quize_Brain

Question_bank=[]

for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text, question_answer)
    Question_bank.append(new_question)

quiz=Quize_Brain(Question_bank)
while quiz.still_have_question:
    quiz.next_question()

print(f"you have completed the quiz\nyour final score is {quiz.score}/{quiz.question_number}")



