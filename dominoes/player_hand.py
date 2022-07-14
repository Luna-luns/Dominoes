from typing import List
from domino import Domino


class PlayerHand:
    def __init__(self, dominoes: List[Domino]):
        self.dominoes = dominoes

    def __str__(self):
        return f'[{",".join([domino.__str__() for domino in self.dominoes])}]'

    def size(self):
        return len(self.dominoes)

    def find_biggest_domino(self) -> Domino:
        biggest_domino = self.dominoes[0]

        for domino in self.dominoes:
            if domino.count_domino_sum() > biggest_domino.count_domino_sum():
                biggest_domino = domino

        return biggest_domino

    def remove_domino(self, domino: Domino) -> None:
        self.dominoes.remove(domino)

    def enumerate(self, start=1) -> enumerate:
        return enumerate(self.dominoes, start=start)

    def take_domino(self, number: int) -> Domino:
        domino = self.dominoes[number - 1]
        self.remove_domino(domino)
        return domino

    def append(self, domino: Domino) -> None:
        self.dominoes.append(domino)

    def insert(self, number: int, domino: Domino) -> None:
        self.dominoes.insert(number - 1, domino)
