class LexerError(Exception):
    """Exception raised for lexer errors."""
    def __init__(self, message, position=None):
        self.message = message
        self.position = position
        super().__init__(self.message)

class ParserError(Exception):
    """Exception raised for parser errors."""
    def __init__(self, message, token=None):
        self.message = message
        self.token = token
        super().__init__(self.message)

class CompilerError(Exception):
    """Exception raised for compiler errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)