class Domino:
    def __init__(self, left_side: int, right_side: int):
        self.left_side = left_side
        self.right_side = right_side

    def is_double(self) -> bool:
        return self.left_side == self.right_side

    def count_domino_sum(self):
        return self.left_side + self.right_side

    def has_side_count(self, side: int):
        result: int = 0
        if self.left_side == side:
            result += 1

        if self.right_side == side:
            result += 1

        return result

    def contain_element(self, element: int) -> bool:
        return self.left_side == element or self.right_side == element

    def switch_sides(self) -> None:
        self.left_side, self.right_side = self.right_side, self.left_side

    def __str__(self):
        return f'[{self.left_side}, {self.right_side}]'
