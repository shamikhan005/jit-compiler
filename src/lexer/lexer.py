from ..utils.errors import LexerError
from .token import Token

class Lexer:
    def __init__(self, text):
        self.text = text.strip()  # Remove leading/trailing whitespace
        self.pos = 0
        self.current_char = self.text[0] if self.text else None

    def error(self, message):
        raise LexerError(f"{message} at position {self.pos}")

    def advance(self):
        """Advance the position pointer and set the current_char."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        """Skip whitespace characters."""
        while self.current_char and self.current_char.isspace():
            self.advance()

    def number(self):
        """Return a number consumed from the input."""
        result = ''
        decimal_point_count = 0

        while self.current_char and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    self.error("Invalid number format: multiple decimal points")
            result += self.current_char
            self.advance()

        try:
            return float(result) if '.' in result else int(result)
        except ValueError:
            self.error(f"Invalid number format: {result}")

    def get_next_token(self):
        """Lexical analyzer (tokenizer)"""
        while self.current_char is not None:
            # Skip whitespace
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            # Handle numbers
            if self.current_char.isdigit() or self.current_char == '.':
                return Token('NUMBER', self.number())

            # Handle operators
            if self.current_char in '+-*/':
                op = self.current_char
                self.advance()
                return Token('OPERATOR', op)

            self.error(f"Invalid character: {self.current_char}")

        return Token('EOF', None)
