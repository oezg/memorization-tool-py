from flashcard import Flashcard


class Tool:
    def __init__(self):
        self.flashcards: list[Flashcard] = []
        self.menu = {
            "1": ("Add flashcards", self.add_flashcards),
            "2": ("Practice flashcards", self.practice_flashcards),
            "3": ("Exit",),
        }

    def add_flashcards(self):
        while (option := input("1. Add a new flashcard\n2. Exit\n")) != "2":
            if option == "1":
                while not (question := input("Question:\n").strip()):
                    ...
                while not (answer := input("Answer:\n").strip()):
                    ...
                self.flashcards.append(Flashcard(question, answer))
            else:
                print(f"{option} is not an option")

    def practice_flashcards(self):
        if self.flashcards:
            for card in self.flashcards:
                template = f'Question: {card.question}\nPlease press "y" to see the answer or press "n" to skip:\n'
                while (option := input(template)) not in ('y', 'n'):
                    print(f"{option} is not an option")
                if option == 'y':
                    print(f"\nAnswer: {card.answer}")
        else:
            print("There is no flashcard to practice!")

    def main(self):
        while (option := self.get_option()) != "3":
            self.menu[option][1]() if option in self.menu else print(f"{option} is not an option")
        print("Bye!")

    def get_menu(self):
        return "\n".join(f"{i}. {option[0]}" for i, option in self.menu.items())

    def get_option(self) -> str:
        return input(self.get_menu() + "\n")


if __name__ == '__main__':
    Tool().main()
