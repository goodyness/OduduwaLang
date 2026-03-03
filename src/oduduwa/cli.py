import argparse
import sys
import os
from oduduwa.core.lexer import OduduwaLexer
from oduduwa.core.parser import OduduwaParser
from oduduwa.core.transpiler import OduduwaTranspiler

def run_file(filepath, debug=False):
    if not os.path.exists(filepath):
        print(f"Aṣiṣe (Error): Kò rí fáyìlì '{filepath}' (File not found).")
        sys.exit(1)
        
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()
        
    try:
        if debug: print("--- Lexing ---")
        lexer = OduduwaLexer(code)
        tokens = lexer.tokenize()
        
        if debug: print("--- Parsing ---")
        parser = OduduwaParser(tokens)
        ast = parser.parse()
        
        if debug: print("--- Transpiling ---")
        transpiler = OduduwaTranspiler()
        python_code = transpiler.transpile(ast)
        
        if debug: 
            print("--- Generated Python Code ---")
            print(python_code)
            print("--- Running ---")
            
        # Prepare the Oduduwa execution environment with the Standard Library
        import oduduwa.stdlib.iro as iro
        
        env_globals = globals().copy()
        env_globals['iro'] = iro
        
        # Execute the generated Python code
        exec(python_code, env_globals)
        
    except Exception as e:
        import sys
        from oduduwa.errors.reporter import handle_exception
        exc_type, exc_value, exc_traceback = sys.exc_info()
        source_lines = code.split('\n') if 'code' in locals() else None
        handle_exception(exc_type, exc_value, exc_traceback, source_lines)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="OduduwaLang - The Yoruba Programming Language")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # "run" command (ṣiṣẹ)
    run_parser = subparsers.add_parser("sise", help="Run an OduduwaLang file (alias: run)")
    run_parser.add_argument("file", help="Path to the .odu file")
    run_parser.add_argument("--debug", action="store_true", help="Print debug information")
    
    run_parser_en = subparsers.add_parser("run", help="Run an OduduwaLang file")
    run_parser_en.add_argument("file", help="Path to the .odu file")
    run_parser_en.add_argument("--debug", action="store_true", help="Print debug information")

    # "repl" command
    repl_parser = subparsers.add_parser("soro", help="Start the Interactive REPL")
    repl_parser_en = subparsers.add_parser("repl", help="Start the Interactive REPL")

    # "format" command
    fmt_parser = subparsers.add_parser("se_eto", help="Format an OduduwaLang file (alias: format)")
    fmt_parser.add_argument("file", help="Path to the .odu file")
    fmt_parser_en = subparsers.add_parser("format", help="Format an OduduwaLang file")
    fmt_parser_en.add_argument("file", help="Path to the .odu file")

    # "lint" command
    lint_parser = subparsers.add_parser("yewo", help="Lint an OduduwaLang file (alias: lint)")
    lint_parser.add_argument("file", help="Path to the .odu file")
    lint_parser_en = subparsers.add_parser("lint", help="Lint an OduduwaLang file")
    lint_parser_en.add_argument("file", help="Path to the .odu file")

    # If no arguments are provided, default to REPL
    if len(sys.argv) == 1:
        from oduduwa.repl import start_repl
        start_repl()
        return

    args = parser.parse_args()
    
    if args.command in ["sise", "run"]:
        run_file(args.file, args.debug)
    elif args.command in ["soro", "repl"]:
        from oduduwa.repl import start_repl
        start_repl()
    elif args.command in ["se_eto", "format"]:
        from oduduwa.core.formatter import format_file
        format_file(args.file)
    elif args.command in ["yewo", "lint"]:
        from oduduwa.core.linter import lint_file
        lint_file(args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
