from question_module import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["category"], question["type"], question["difficulty"], question["question"], question["correct_answer"], question["incorrect_answers"]))

quiz = QuizBrain(question_bank)

game_is_over = False
while quiz.still_has_questions():
    quiz.next_question()
quiz.final_score()

