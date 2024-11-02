from ..lexer.lexer import Lexer
from ..utils.errors import CompilerError

class JITCompiler:
    def __init__(self):
        self.lexer = None

    def compile(self, text):
        """Compile and execute the given text."""
        try:
            # Initialize lexer with input text
            self.lexer = Lexer(text)
            
            # Evaluate the expression
            result = self._evaluate_expression()
            
            return result
        except Exception as e:
            raise CompilerError(f"Invalid expression: {str(e)}")

    def _evaluate_expression(self):
        """Evaluate a simple arithmetic expression."""
        # Get the first number
        token = self.lexer.get_next_token()
        if token.type != 'NUMBER':
            raise CompilerError("Expression must start with a number")
        
        result = token.value
        
        # Process the rest of the expression
        while True:
            # Get the operator
            token = self.lexer.get_next_token()
            if token.type == 'EOF':
                break
                
            if token.type != 'OPERATOR':
                raise CompilerError(f"Expected operator, got {token.type}")
            
            operator = token.value
            
            # Get the next number
            token = self.lexer.get_next_token()
            if token.type != 'NUMBER':
                raise CompilerError(f"Expected number after operator, got {token.type}")
            
            # Perform the operation
            if operator == '+':
                result += token.value
            elif operator == '-':
                result -= token.value
            elif operator == '*':
                result *= token.value
            elif operator == '/':
                if token.value == 0:
                    raise CompilerError("Division by zero")
                result /= token.value
        
        return result
