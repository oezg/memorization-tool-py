from flashcard import Flashcard, get_session


def get_option(menu, *alternatives):
    while (option := input(menu + '\n')) not in alternatives:
        print(f"{option} is not an option")
    return option


class Tool:
    def __init__(self) -> None:
        self.session = get_session()

    def main(self) -> None:
        option = get_option('1. Add flashcards\n2. Practice flashcards\n3. Exit', '1', '2', '3')
        if option == '1':
            self.add_flashcards()
        elif option == '2':
            self.practice_flashcards()
        print("Bye!")

    def add_flashcards(self) -> None:
        option = get_option("1. Add a new flashcard\n2. Exit", '1', '2')
        if option == "1":
            while not (question := input("Question:\n").strip()):
                ...
            while not (answer := input("Answer:\n").strip()):
                ...
            card = Flashcard(question=question, answer=answer)
            self.session.add(card)
            self.session.commit()
            self.add_flashcards()

    def practice_flashcards(self) -> None:
        flashcards = self.session.query(Flashcard)
        if not flashcards.all():
            print("There is no flashcard to practice!")
            return
        for card in flashcards.all():
            print(f'Question: {card.question}')
            option = get_option('press "y" to see the answer:\npress "n" to skip:\npress "u" to update:', 'y', 'n', 'u')
            if option == 'u':
                self.update_flashcard(card)
            elif option == 'y':
                self.test_flashcard(card)
        flashcards.filter(Flashcard.repetition == 3).delete()
        self.session.commit()

    def test_flashcard(self, card) -> None:
        print(f"Answer: {card.answer}")
        option = get_option('press "y" if your answer is correct:\npress "n" if your answer is wrong:', 'y', 'n')
        self.session.query(Flashcard).filter(Flashcard.id == card.id)\
            .update({'repetition': Flashcard.repetition + 1 if option == 'y' else 0})

    def update_flashcard(self, card) -> None:
        option = get_option('press "d" to delete the flashcard:\npress "e" to edit the flashcard:', 'd', 'e')
        if option == 'd':
            self.session.delete(card)
            return
        new_fields = {key: value for key, value in {
            'question': input(f"current question: {card.question}\nplease write a new question:\n"),
            'answer': input(f"current answer: {card.answer}\nplease write a new answer:\n")
        }.items() if value}
        if new_fields:
            self.session.query(Flashcard).filter(Flashcard.id == card.id).update(new_fields)


if __name__ == '__main__':
    Tool().main()
