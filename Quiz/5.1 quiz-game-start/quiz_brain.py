class QuizBrain():
    def __init__(self,question_list):
        self.question_number = 0
        self.question_lis = question_list
        self.score = 0

    def still_has_questins(self):
        if self.question_number != len(self.question_lis):
            return True
        else:
            return False
        
    def next_question(self):
        question = self.question_lis[self.question_number].text
        q_answer = self.question_lis[self.question_number].answer
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question} (True/False)?: ").capitalize()
        self.check_answer(answer,q_answer)


    def check_answer(self,answer,q_answer):

        if answer == q_answer:
            print("You Got It Right!")
            self.score += 1
        else:
            print("You Got it Wrong")
        print(f"The Correct answer was: {q_answer}")
        print(f"Current Score: {self.score}")
        print()
        

