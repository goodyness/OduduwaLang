from oduduwa.core.lexer import OduduwaLexer
from oduduwa.core.parser import OduduwaParser
from oduduwa.core.ast import *

def dump_ast(node, indent=0):
    """Simple debugging function to print the AST tree."""
    prefix = "  " * indent
    if isinstance(node, list):
        for n in node:
            dump_ast(n, indent)
    elif isinstance(node, Module):
        print(f"{prefix}Module:")
        dump_ast(node.body, indent + 1)
    elif isinstance(node, FunctionDef):
        args = ", ".join([a.id for a in node.args])
        print(f"{prefix}FunctionDef(name={node.name}, args=[{args}])")
        dump_ast(node.body, indent + 1)
    elif isinstance(node, If):
        print(f"{prefix}If:")
        print(f"{prefix}  Condition:")
        dump_ast(node.condition, indent + 2)
        print(f"{prefix}  Body:")
        dump_ast(node.body, indent + 2)
        if node.orelse:
            print(f"{prefix}  OrElse:")
            dump_ast(node.orelse, indent + 2)
    elif isinstance(node, Call):
        print(f"{prefix}Call(func={node.func.id})")
        for arg in node.args:
            dump_ast(arg, indent + 1)
    elif isinstance(node, Assign):
        print(f"{prefix}Assign(target={node.target.id})")
        dump_ast(node.value, indent + 1)
    elif isinstance(node, Return):
        print(f"{prefix}Return:")
        dump_ast(node.value, indent + 1)
    elif isinstance(node, BinOp):
        print(f"{prefix}BinOp(op='{node.op}')")
        dump_ast(node.left, indent + 1)
        dump_ast(node.right, indent + 1)
    elif isinstance(node, Name):
        print(f"{prefix}Name(id={node.id})")
    elif isinstance(node, String):
        print(f"{prefix}String('{node.s}')")
    elif isinstance(node, Number):
        print(f"{prefix}Number({node.n})")
    else:
        print(f"{prefix}{type(node).__name__}()")

def test_parser():
    code = """
ise se_oniruru(x):
    ye_x = x * 2
    ti ye_x > 10:
        tejade("O tobi!")
    bibeeko:
        tejade("O kekere")
    pada ye_x

abajade = se_oniruru(5)
tejade(abajade)
"""
    lexer = OduduwaLexer(code)
    tokens = lexer.tokenize()
    parser = OduduwaParser(tokens)
    
    ast = parser.parse()
    dump_ast(ast)
    print("\n✓ Parsing completed!")

if __name__ == "__main__":
    test_parser()
