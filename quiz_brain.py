class Quize_Brain:
    
    def __init__(self, q_list):
        self.question_number=0
        self.question_bank=q_list
        self.score=0

    def still_have_question(self):
        if self.question_number<(len(self.question_bank)):
            return True
        else:
            return False
        

    def next_question(self):
        current_question=self.question_bank[self.question_number]
        self.question_number+=1
        current_answer=input(f"Q.{self.question_number}:{current_question.text}(True/False):\n")
        self.check_answer(current_question.answer, current_answer)

    def check_answer(self, current_question, current_answer):
        if current_answer.lower()== current_question.lower():
            self.score+=1
            print(f"you got it right !\nthe correct answer was : {current_question}")
        else:
            print(f"wrong answer\nthe correct answer was : {current_question}")
        print(f"your current score is {self.score}/{self.question_number}\n")
