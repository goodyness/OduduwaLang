import os
import sys
from oduduwa.core.lexer import OduduwaLexer
from oduduwa.core.parser import OduduwaParser

def lint_file(filepath):
    """
    yẹwò (Lint) an OduduwaLang file for syntax errors without executing it.
    """
    if not os.path.exists(filepath):
        print(f"Aṣiṣe (Error): Kò rí fáyìlì '{filepath}' (File not found).")
        sys.exit(1)
        
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()
        
    try:
        lexer = OduduwaLexer(code)
        tokens = list(lexer.tokenize())
        parser = OduduwaParser(tokens)
        ast = parser.parse()
        print(f"✅ Ayewo Kọja (Linting Passed): Fáyìlì '{filepath}' dára.")
    except Exception as e:
        import sys
        from oduduwa.errors.reporter import handle_exception
        exc_type, exc_value, exc_traceback = sys.exc_info()
        source_lines = code.split('\n')
        print(f"❌ OduduwaLint Ri Asiṣe (Linter Found Errors) ninu '{filepath}':")
        handle_exception(exc_type, exc_value, exc_traceback, source_lines)
        sys.exit(1)
