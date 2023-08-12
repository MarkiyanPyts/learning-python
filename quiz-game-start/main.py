from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    questions_bank.append(new_question)

quiz = QuizBrain(questions_bank)
quiz.next_question()