class IllegalMoveError(Exception):
    def __str__(self) -> str:
        return 'Illegal move. Please try again.'
