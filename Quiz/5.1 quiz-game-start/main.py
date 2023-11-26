from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions = question_data
data_objcets = []
for q in questions:
    data_objcets.append(Question(q['text'],q['answer']))

quiz = QuizBrain(data_objcets)

while quiz.still_has_questins():
     guess = quiz.next_question()

print(f"Your Final Score is: {quiz.score}")