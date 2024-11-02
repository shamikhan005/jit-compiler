# JIT Compiler for Scripting Languages

*this is an academic/university project, not a personal project.*

A Just-In-Time (JIT) compiler that interprets and compiles simple arithmetic expressions, such as addition, subtraction, multiplication, and division. It translates these expressions into x86-64 machine code and executes them at runtime.

## Features

- **Arithmetic Operations**: Supports +, -, *, and /
- **JIT Compilation**: Translates expressions to machine code on the fly
- **Memory Management**: Manages memory allocation for machine code execution
- **Error Handling**: Basic error handling for lexer and syntax errors

## Installation

To run this project, make sure you have Python 3.x installed along with ctypes and mmap (both are included in the standard library).

### Dependencies

Install any dependencies with:

```bash
pip install -r requirements.txt
```
## Usage

To run the provided example, execute:

```bash
python examples/simple_arithmetic.py
```
Example Output

![Screenshot 2024-11-02 193522](https://github.com/user-attachments/assets/52c735dc-232b-4f38-b78a-cd362be85eca)

## How It Works

1. **Lexing**: 
   - The `Lexer` class in `src/lexer/lexer.py` tokenizes the input expression.

2. **Parsing & Code Generation**: 
   - Tokens are converted into machine code instructions by `CodeGenerator` in `src/compiler/code_gen.py`.

3. **Memory Allocation & Execution**: 
   - The `MemoryManager` class in `src/compiler/memory.py` handles memory allocation and creates executable function pointers.

4. **Compilation**: 
   - `JITCompiler` compiles and executes expressions, caching the compiled code for reuse.

## Error Handling

The JIT compiler has basic error handling for:

- **Invalid characters** in the lexer (`LexerError`)
- **Invalid expressions** due to syntax errors
