#!/usr/bin/env python

"""A kids game intended for learning addition of integer numbers"""

import random
import sys

__author__ = "Léon Spaans"
__date__ = "2017-03-13"
__version__ = "0.1.0"


class _Game(object):
    """An interface-like class for games"""

    def __init__(self, rounds=10):
        """
        Constructor method.

        Arguments:
            rounds - int(): number of rounds
        """
        self.name = ""
        self.round_number = 1
        self.rounds = rounds

        self._init_game()

    def _init_game(self):
        """
        Initializes the game.
        """
        try:
            self._init_name()
        except KeyboardInterrupt:
            sys.exit("")

    def _init_name(self):
        """
        Initializes the player name from keyboard.
        """
        name = ""

        while name == "":
            name = input("Wat is je naam? ")

        self.name = name.capitalize()

        print("{greet} {name}!\n".format(
            **dict({
                "greet": random.choice([
                    "welkom", "hoi", "hallo", "dag", "hé", "ha die"
                ]).capitalize()
                }, **self.__dict__)
        ))


class LovingNumbers(_Game):
    """A kids game intended for learning addition of integer numbers"""

    def __init__(self, rounds=10):
        """
        Constuctor method.

        Arguments:
            rounds - int(): number of rounds
        """
        super().__init__(rounds)

        self.answer = ""
        self.maximum = 0
        self.number_a = 0
        self.number_b = 0
        self.right = 0
        self.variable = ""
        self.wrong = 0

        self._init_maximum()

        self.numbers = list(range(self.maximum))

    def _do_round(self):
        """
        Starts next round.
        """
        self.answer = ""
        self.number_a = self._get_number()
        self.number_b = self.maximum - self.number_a
        self.variable = random.choice(["a", "b"])

        self.answer = self._get_answer()

        self._process_score()

        self.round_number += 1

    def _get_answer(self):
        """
        Arguments:
        """
        answer = ""

        print(
            (
                "\n{round_number}e ronde ({right} goed/{wrong} fout): " +
                "{a} + {b} = {maximum}"
            ).format(**dict({
                "a": self.number_a if self.variable == "b" else "?",
                "b": self.number_b if self.variable == "a" else "?"
            }, **self.__dict__))
        )

        while not answer.isdigit():
            answer = input("Wat is het antwoord: ")

        return int(answer)

    def _get_comment(self):
        """
        Arguments:
        """
        comments = [
            "Jammer! Volgende keer beter!",
            "Als je veel oefent word je vanzelf beter!",
            "Blijven proberen!",
            "Goed geprobeerd!",
            "Je doet je best, maar het moet nog wat beter",
            "Je hebt bijna een voldoende!",
            "Mooi hoor! Een voldoende!",
            "Fijn! Dat is een mooi resultaat",
            "Knap hoor! Dat is een heel mooi resultaat",
            "Sjonge, je hebt bijna alles goed!",
            "Fantastisch, je hebt alles goed! Slimmerd!"
        ]
        return comments[
            len(comments) - 1 if self.right > len(comments) - 1 else self.right
        ]

    def _get_number(self):
        """
        Arguments:
        """
        return self.numbers.pop(
            random.choice(range(len(self.numbers)))
        )

    def _init_maximum(self):
        """
        Arguments:
        """
        maximum = ""

        while not maximum.isdigit() or int(maximum) < 10:
            maximum = input(
                "Hoe hoog moeten de verliefde getallen samen zijn? "
            )

        self.maximum = int(maximum)

        print("{maximum} is een {type} keuze!".format(
            **dict({
                "type": random.choice([
                    "mooie", "slimme", "prima", "goeie", "top"
                ]),
            }, **self.__dict__)
        ))

    def _main_loop(self):
        """
        Arguments:
        """
        try:
            while self.round_number <= self.rounds:
                self._do_round()
        except KeyboardInterrupt:
            print("\nTot de volgende keer!")

    def _process_score(self):
        """
        Arguments:
        """
        number = self.number_a if self.variable == "a" else self.number_b

        if number == self.answer:
            print("\nDat is goed. {type} hoor!".format(
                **dict({
                    "type": random.choice([
                        "knap", "slim", "mooi", "gaaf", "leuk"
                    ]).capitalize()
                }, **self.__dict__)
            ))

            self.right += 1
        else:
            print("\nDat is niet goed. {comment}!".format(
                **dict({
                    "comment": random.choice([
                        "zet 'm op", "kom op", "blijven proberen"
                    ]).capitalize()
                }, **self.__dict__)
            ))
            print(
                (
                    "Het goede antwoord is {number} want " +
                    "{number_a} + {number_b} = {maximum}"
                ).format(**dict({"number": number}, **self.__dict__))
            )

            self.wrong += 1

    def _show_goodbye(self):
        """
        Arguments:
        """
        print("Tot {wish} {name}. {goodbye}!\n".format(
            **dict({
                "wish": random.choice([
                    "snel", "gauw", "ziens", "kijk"
                ]),
                "goodbye": random.choice([
                    "doei", "doeg", "dag", "houdoe"
                ]).capitalize()
                }, **self.__dict__)
        ))

    def _show_statistics(self):
        """
        Arguments:
        """
        print(
            (
                "\nDat was het!\n\nJe hebt {right} antwoord{rmul} goed " +
                "en {wrong} antwoord{wmul} fout.\n\n{comment}\n"
            ).format(**dict({
                "comment": self._get_comment(),
                "rmul": "en" if self.right != 1 else "",
                "wmul": "en" if self.wrong != 1 else ""
            }, **self.__dict__))
        )

    def _show_welcome(self):
        """
        Arguments:
        """
        print("\nWe gaan beginnen! Er zijn {rounds} ronden.".format(
            **self.__dict__
        ))

    def start(self):
        """
        Arguments:
        """
        self._main_loop()
        self._show_statistics()
        self._show_goodbye()


def main():
    """
    Arguments:
    """
    LovingNumbers().start()


if __name__ == "__main__":
    """
    The main function that is automatically called when the script itself is
    executed.
    """
    main()
