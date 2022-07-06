class UserInterface:
    def ask_command(self) -> str:
        return input().strip()

    def is_input_number(self, command: str) -> bool:
        return command.lstrip('-').isdigit()


