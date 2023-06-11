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
        if flashcards.all():
            for card in flashcards.all():
                template = f'Question: {card.question}\npress "y" to see the answer:\npress "n" to skip:\npress "u" to update:\n'
                while (option := input(template)) not in ('y', 'n', 'u'):
                    print(f"{option} is not an option")
                match option:
                    case 'y':
                        print(f"\nAnswer: {card.answer}")
                    case 'u':
                        while (update_option := input('press "d" to delete the flashcard:\npress "e" to edit the flashcard:\n')) not in ('d', 'e'):
                            print(f"{update_option} is not an option")
                        match update_option:
                            case 'e':
                                new_question = input(f"current question: {card.question}\nplease write a new question:\n")
                                if new_question:
                                    flashcards.filter(flashcard.Flashcard.id == card.id).update({'question': new_question})
                                new_answer = input(f"current answer: {card.answer}\nplease write a new answer:\n")
                                if new_answer:
                                    flashcards.filter(flashcard.Flashcard.id == card.id).update({'answer': new_answer})
                                self.session.commit()
                            case 'd':
                                flashcards.filter(flashcard.Flashcard.id == card.id).delete()
                                self.session.commit()
        else:
            print("There are no flashcards to practice!")

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
