from oduduwa.core.lexer import OduduwaLexer
from oduduwa.core.parser import OduduwaParser
from oduduwa.core.transpiler import OduduwaTranspiler

def test_transpiler():
    code = """
# OduduwaLang Example: Factorial
ise se_ifosi(n):
    ti n == 1:
        pada 1
    bibeeko:
        pada n * se_ifosi(n - 1)

abajade = se_ifosi(5)
tejade("Abajade jẹ: ", abajade)
"""
    print("--- Original Oduduwa Code ---")
    print(code)
    
    lexer = OduduwaLexer(code)
    tokens = lexer.tokenize()
    
    parser = OduduwaParser(tokens)
    ast = parser.parse()
    
    transpiler = OduduwaTranspiler()
    python_code = transpiler.transpile(ast)
    
    print("\n--- Transpiled Python Code ---")
    print(python_code)
    
    print("\n✓ Transpilation completed!")
    
    print("\n--- Running Python Code ---")
    exec(python_code, globals())

if __name__ == "__main__":
    test_transpiler()
