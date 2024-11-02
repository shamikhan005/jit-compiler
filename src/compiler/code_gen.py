import struct
from typing import List, Dict
from ..lexer.token import Token, TokenType

class CodeGenerator:
    def __init__(self):
        # x86-64 machine code templates
        self.prologue = bytes([
            0x55,                   # push rbp
            0x48, 0x89, 0xe5,      # mov rbp, rsp
        ])
        
        self.epilogue = bytes([
            0x48, 0x89, 0xec,      # mov rsp, rbp
            0x5d,                   # pop rbp
            0xc3,                   # ret
        ])

        # Instruction templates
        self.instructions = {
            TokenType.PLUS: bytes([0xf2, 0x0f, 0x58, 0xc1]),     # addsd xmm0, xmm1
            TokenType.MINUS: bytes([0xf2, 0x0f, 0x5c, 0xc1]),    # subsd xmm0, xmm1
            TokenType.MULTIPLY: bytes([0xf2, 0x0f, 0x59, 0xc1]), # mulsd xmm0, xmm1
            TokenType.DIVIDE: bytes([0xf2, 0x0f, 0x5e, 0xc1]),   # divsd xmm0, xmm1
        }

    def generate_number_load(self, value: float) -> bytes:
        """Generate code to load a number into a register."""
        # mov rax, immediate value
        prefix = bytes([0x48, 0xb8])
        number_bytes = struct.pack('<d', value)
        return prefix + number_bytes

    def generate_code(self, tokens: List[Token]) -> bytes:
        """Generate machine code from tokens."""
        machine_code = bytearray(self.prologue)
        stack = []

        for token in tokens:
            if token.type == TokenType.NUMBER:
                machine_code.extend(self.generate_number_load(token.value))
                stack.append('rax')
            
            elif token.type in self.instructions:
                if len(stack) < 2:
                    raise SyntaxError("Invalid expression")
                
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                machine_code.extend(self.instructions[token.type])
                stack.append('xmm0')

        machine_code.extend(self.epilogue)
        return bytes(machine_code)