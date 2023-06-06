class Flashcard:
    def __init__(self, question, answer):
        self._question = question
        self._answer = answer

    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, value):
        self._question = value

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        self._answer = value
