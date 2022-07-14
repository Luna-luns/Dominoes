from domino import Domino
from typing import List
from illegal_move_error import IllegalMoveError


class Field:
    def __init__(self):
        self.field_list: List[Domino] = []

    def append_left(self, domino: Domino):
        if not len(self.field_list) == 0 and not domino.contain_element(self.get_left().left_side):
            raise IllegalMoveError()

        if len(self.field_list) != 0 and domino.right_side != self.get_left().left_side:
            domino.switch_sides()

        self.field_list.insert(0, domino)

    def append_right(self, domino: Domino) -> None:
        if not len(self.field_list) == 0 and not domino.contain_element(self.get_right().right_side):
            raise IllegalMoveError()

        if len(self.field_list) != 0 and domino.left_side != self.get_right().right_side:
            domino.switch_sides()

        self.field_list.append(domino)

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

    def __str__(self):
        if len(self.field_list) > 6:
            return f'{"".join([self.field_list[i].__str__() for i in range(3)])}' \
                   f'...' \
                   f'{"".join([self.field_list[-3 + i].__str__() for i in range(3)])}'

        return "".join([domino.__str__() for domino in self.field_list])
