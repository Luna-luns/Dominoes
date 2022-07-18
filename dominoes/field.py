from domino import Domino
from typing import List
from illegal_move_error import IllegalMoveError


class Direction:
    def __init__(self, _id: int):
        self.id = _id


ALL = Direction(0)
RIGHT = Direction(1)
LEFT = Direction(2)


class Field:
    def __init__(self):
        self.field_list: List[Domino] = []

    def append_left(self, domino: Domino):
        if not self.is_appropriate(domino, LEFT):
            raise IllegalMoveError()

        if len(self.field_list) != 0 and domino.right_side != self.get_left().left_side:
            domino.switch_sides()

        self.field_list.insert(0, domino)

    def append_right(self, domino: Domino) -> None:
        if not self.is_appropriate(domino, RIGHT):
            raise IllegalMoveError()

        if len(self.field_list) != 0 and domino.left_side != self.get_right().right_side:
            domino.switch_sides()

        self.field_list.append(domino)

    def is_appropriate(self, domino: Domino, direction: Direction) -> bool:
        if len(self.field_list) == 0:
            return True

        is_right = domino.contain_element(self.get_right().right_side)
        if direction == RIGHT:
            return is_right

        is_left = domino.contain_element(self.get_left().left_side)
        if direction == LEFT:
            return is_left

        if direction == ALL:
            return is_left or is_right

    def is_draw(self) -> bool:
        left: int = self.field_list[0].left_side
        right: int = self.field_list[len(self.field_list) - 1].right_side
        if left != right:
            return False

        count: int = 0
        for domino in self.field_list:
            count += domino.has_side_count(left)

        if count != 8:
            return False

        return True

    def get_left(self) -> Domino:
        return self.field_list[0]

    def get_right(self) -> Domino:
        return self.field_list[len(self.field_list) - 1]

    def count_numbers(self) -> dict:
        dictionary = {}
        for domino in self.field_list:
            for num in domino:
                dictionary[num] = dictionary.get(num, 0) + 1

            return dictionary

    def __str__(self):
        if len(self.field_list) > 6:
            return f'{"".join([self.field_list[i].__str__() for i in range(3)])}' \
                   f'...' \
                   f'{"".join([self.field_list[-3 + i].__str__() for i in range(3)])}'

        return "".join([domino.__str__() for domino in self.field_list])
