import random
from domino import Domino
from player_hand import PlayerHand


class DominoStock:
    def __init__(self, domino_list: list):
        self.domino_list = domino_list

    def __str__(self):
        return f'[{",".join([domino.__str__() for domino in self.domino_list])}]'

    def take_hand(self) -> PlayerHand:
        has_double = False
        player_hand = []
        while not has_double:
            player_hand = random.sample(self.domino_list, 7)
            for domino in player_hand:
                if domino.is_double():
                    has_double = True

        for domino in player_hand:
            self.domino_list.remove(domino)

        return PlayerHand(player_hand)

    def size(self):
        return len(self.domino_list)

    def take_random_domino(self) -> Domino:
        domino = random.choice(self.domino_list)
        self.domino_list.remove(domino)
        return domino

    def is_empty(self) -> bool:
        return len(self.domino_list) == 0


def from_raw_list(raw_list: list) -> DominoStock:
    return DominoStock([Domino(elem[0], elem[1]) for elem in raw_list])
