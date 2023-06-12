import flashcard


class Tool:
    def __init__(self) -> None:
        self.session = flashcard.get_session()
        self.menu = {
            "1": ("Add flashcards", self.add_flashcards),
            "2": ("Practice flashcards", self.practice_flashcards),
            "3": ("Exit",),
        }

    def add_flashcards(self) -> None:
        while (option := input("1. Add a new flashcard\n2. Exit\n")) != "2":
            if option == "1":
                while not (question := input("Question:\n").strip()):
                    ...
                while not (answer := input("Answer:\n").strip()):
                    ...
                card = flashcard.Flashcard(question=question, answer=answer)
                self.session.add(card)
                self.session.commit()
            else:
                print(f"{option} is not an option")

    def practice_flashcards(self) -> None:
        flashcards = self.session.query(flashcard.Flashcard)
        if not flashcards.all():
            print("There is no flashcard to practice!")
            return
        for card in flashcards.all():
            print(f'Question: {card.question}\npress "y" to see the answer:\npress "n" to skip:\npress "u" to update:')
            while (option := input()) not in ('y', 'n', 'u'):
                print(f"{option} is not an option")
            if option == 'u':
                print('press "d" to delete the flashcard:\npress "e" to edit the flashcard:')
                while (update_option := input()) not in ('d', 'e'):
                    print(f"{update_option} is not an option")
                if update_option == 'e':
                    new_fields = {key: value for key, value in {
                        'question': input(f"current question: {card.question}\nplease write a new question:\n"),
                        'answer': input(f"current answer: {card.answer}\nplease write a new answer:\n")
                    }.items() if value}
                    if new_fields:
                        flashcards.filter(flashcard.Flashcard.id == card.id).update(new_fields)
                elif update_option == 'd':
                    self.session.delete(card)
            elif option == 'y':
                print(f"\nAnswer: {card.answer}")
                print('press "y" if your answer is correct:\npress "n" if your answer is wrong:')
                while (learn_success := input()) not in ('y', 'n'):
                    print(f"{learn_success} is not an option")
                if learn_success == 'y':
                    flashcards.filter(flashcard.Flashcard.id == card.id).update({'box': flashcard.Flashcard.box + 1})
                else:
                    flashcards.filter(flashcard.Flashcard.id == card.id).update({'box': 0})
        flashcards.filter(flashcard.Flashcard.box == 3).delete()
        self.session.commit()

    def main(self) -> None:
        while (option := self.get_option()) != "3":
            self.menu[option][1]() if option in self.menu else print(f"{option} is not an option")
        print("Bye!")

    def get_menu(self) -> str:
        return "\n".join(f"{i}. {option[0]}" for i, option in self.menu.items())

    def get_option(self) -> str:
        return input(self.get_menu() + "\n")


if __name__ == '__main__':
    Tool().main()
