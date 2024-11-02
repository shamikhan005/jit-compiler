from enum import Enum, auto
from typing import Any

class TokenType(Enum):
    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    EOF = auto()

class Token:
    def __init__(self, type: TokenType, value: Any = None):
        self.type = type
        self.value = value
    
    def __str__(self):
        return f'Token({self.type}, {self.value})'
    
    def __repr__(self):
        return self.__str__()