class Flashcard:
    def __init__(self, question: str, answer: str) -> None:
        self._question = question
        self._answer = answer

    @property
    def question(self) -> str:
        return self._question

    @question.setter
    def question(self, value) -> None:
        self._question = value

    @property
    def answer(self) -> str:
        return self._answer

    @answer.setter
    def answer(self, value) ->None:
        self._answer = value
