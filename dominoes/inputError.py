class InputError(Exception):
    def __str__(self) -> str:
        return 'Invalid input. Please try again.'
