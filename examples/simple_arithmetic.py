import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from src.compiler.jit_compiler import JITCompiler

def main():
    
    jit = JITCompiler()

    test_expressions = [
        "2 + 3",
        "4 * 5",
        "10 / 2",
        "3 - 1",
        "2.5 + 3.7",
        "10 * 2.5"
    ]
   
    for expr in test_expressions:
        try:
            result = jit.compile(expr)
            print(f"Expression: {expr}")
            print(f"Result: {result}")
            print("-" * 20)
        except Exception as e:
            print(f"Error evaluating {expr}: {str(e)}")
            print("-" * 20)

if __name__ == "__main__":
    main()
