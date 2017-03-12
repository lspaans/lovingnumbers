#!/usr/bin/env python

"""Een rekenspelletje over verliefde getallen"""

import locale
import math
import random
import sys

__author__ = "Léon Spaans"
__date__ = "2017-03-12"
__version__ = "0.1.0"


class Game(object):

    def __init__(self, rounds=10):
        self._props = {
            "round_number": 1,
            "rounds": rounds
        }

        self._init_game()

    def _init_game(self):
        try:
            self._init_name()
        except KeyboardInterrupt:
            print()
            sys.exit(0)

    def _init_name(self):
        name = ""

        while name == "":
            name = input("Wat is je naam? ")

        self._props["name"] = name.capitalize()

        print("{greet} {name}!\n".format(**dict({
                "greet": random.choice([
                    "Welkom", "Hoi", "Hallo", "Dag", "Leuk"
                ]),
            }, **self._props
        )))

    @property
    def round_number(self):
        return self._props["round_number"]

    @round_number.setter
    def round_number(self, round_number):
        self._props["round_number"] = round_number

    @property
    def rounds(self):
        return self._props["rounds"]


class LovingNumbers(Game):

    def __init__(self, rounds=10):
        super().__init__(rounds)

        self._init_maximum()
        self._props.update({
            "numbers": list(range(self.maximum)),
            "answer": "",
            "right": 0,
            "wrong": 0
        })

    def _do_round(self):
        self.answer = ""
        self.number_a = self._get_number()
        self.number_b = self.maximum - self.number_a
        self.variable = random.choice(["a", "b"])

        print("\n{round_number}e ronde: {a} + {b} = {maximum}".format(**dict({
                "a": self.number_a if self.variable == "b" else "?",
                "b": self.number_b if self.variable == "a" else "?"
            }, **self._props
        )))

        while not self.answer.isdigit():
            self.answer = input("Wat is het antwoord: ")

        self.answer = int(self.answer)

        self._process_score()

        self.round_number += 1

    def _get_comment(self):
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
        return self._props["numbers"].pop(
            random.choice(range(len(self._props["numbers"])))
        )

    def _init_maximum(self):
        maximum = ""

        while not maximum.isdigit() or int(maximum) < 10:
            maximum = input(
                "Hoe hoog moeten de verliefde getallen samen zijn? "
            )

        self.maximum = int(maximum)

        print("{maximum} is een {type} keuze!".format(**dict({
                "type": random.choice([
                    "mooie", "slimme", "prima", "goeie", "top"
                ]),
            }, **self._props
        )))

    def _main_loop(self):
        try:
            while self.round_number <= self.rounds:
                self._do_round()
        except KeyboardInterrupt:
            print("\nTot de volgende keer!")

    def _process_score(self):
        number = self.number_a if self.variable == "a" else self.number_b

        if number == self.answer:
            print("\nDat is goed. {type} hoor!".format(**dict({
                    "type": random.choice([
                        "Knap", "Slim", "Mooi", "Gaaf", "Leuk"
                    ])
                }, **self._props
            )))

            self.right += 1
        else:
            print("\nDat is niet goed. {comment}!".format(**dict({
                    "comment": random.choice([
                        "Zet 'm op", "Kom op", "Blijven proberen"
                    ])
                }, **self._props
            )))
            print((
                    "Het goede antwoord is {number} want " +
                    "{number_a} + {number_b} = {maximum}"
                ).format(**dict({
                    "number": number
                }, **self._props
            )))

            self.wrong += 1

    def _show_goodbye(self):
        print("Tot {wish} {name}!\n".format(**dict({
                "wish": random.choice([
                    "snel", "gauw", "ziens", "kijk"
                ])
            }, **self._props
        )))

    def _show_statistics(self):
        print(
            (
                "\nDat was het!\n\nJe hebt {right} antwoord{rmul} goed " +
                "en {wrong} antwoord{wmul} fout.\n\n{comment}\n"
                ).format(**dict({
                    "comment": self._get_comment(),
                    "rmul": "en" if self.right != 1 else "",
                    "wmul": "en" if self.wrong != 1 else ""
                }, **self._props
        )))


    def _show_welcome(self):
        print("\nWe gaan beginnen! Er zijn {rounds} ronden.".format(
            **self._props
        ))

    def start(self):
        self._show_welcome()
        self._main_loop()
        self._show_statistics()
        self._show_goodbye()

    @property
    def answer(self):
        return self._props["answer"]

    @answer.setter
    def answer(self, answer):
        self._props["answer"] = answer

    @property
    def maximum(self):
        return self._props["maximum"]

    @maximum.setter
    def maximum(self, maximum):
        self._props["maximum"] = maximum

    @property
    def number_a(self):
        return self._props["number_a"]

    @number_a.setter
    def number_a(self, number_a):
        self._props["number_a"] = number_a

    @property
    def number_b(self):
        return self._props["number_b"]

    @number_b.setter
    def number_b(self, number_b):
        self._props["number_b"] = number_b

    @property
    def right(self):
        return self._props["right"]

    @right.setter
    def right(self, right):
        self._props["right"] = right

    @property
    def variable(self):
        return self._props["variable"]

    @variable.setter
    def variable(self, variable):
        self._props["variable"] = variable

    @property
    def wrong(self):
        return self._props["wrong"]

    @wrong.setter
    def wrong(self, wrong):
        self._props["wrong"] = wrong


def main():
    LovingNumbers().start()


if __name__ == "__main__":
    main()
