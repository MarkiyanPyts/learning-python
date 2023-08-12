class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

new_q = Question("What is the capital of France?", "Paris")
print(new_q.text)
print(new_q.answer)