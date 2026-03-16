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

    # "build" command (kiko/ko)
    build_parser = subparsers.add_parser("kiko", help="Build a standalone Python script (alias: build, ko)")
    build_parser.add_argument("file", help="Path to the .odu file")
    build_parser.add_argument("-o", "--output", help="Output file path")
    
    build_parser_ko = subparsers.add_parser("ko", help="Build a standalone Python script")
    build_parser_ko.add_argument("file", help="Path to the .odu file")
    build_parser_ko.add_argument("-o", "--output", help="Output file path")

    build_parser_en = subparsers.add_parser("build", help="Build a standalone Python script")
    build_parser_en.add_argument("file", help="Path to the .odu file")
    build_parser_en.add_argument("-o", "--output", help="Output file path")

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
    elif args.command in ["kiko", "ko", "build"]:
        build_standalone(args.file, args.output)
    else:
        parser.print_help()

def build_standalone(filepath, output_path=None):
    if not os.path.exists(filepath):
        print(f"Aṣiṣe (Error): Kò rí fáyìlì '{filepath}' (File not found).")
        sys.exit(1)
        
    if output_path is None:
        output_path = filepath.rsplit('.', 1)[0] + ".py"
        
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()
        
    try:
        lexer = OduduwaLexer(code)
        tokens = lexer.tokenize()
        parser = OduduwaParser(tokens)
        ast = parser.parse()
        transpiler = OduduwaTranspiler()
        python_code = transpiler.transpile(ast)
        
        # Simple bundling: Add stdlib contents to the top if used
        bundled_code = "#!/usr/bin/env python3\n# Built with OduduwaLang\n\n"
        
        # Check for imports in the code to include relevant stdlib
        included_modules = []
        for mod in transpiler.STDLIB:
            if f"import {mod}" in python_code or f"from {mod}" in python_code:
                included_modules.append(mod)
        
        if included_modules:
            bundled_code += "import sys, types\n"
            bundled_code += "oduduwa_stdlib = {}\n"
            for mod in included_modules:
                mod_path = os.path.join(os.path.dirname(__file__), "stdlib", f"{mod}.py")
                if os.path.exists(mod_path):
                    with open(mod_path, 'r', encoding='utf-8') as mf:
                        m_content = mf.read()
                    bundled_code += f"\n# --- stdlib: {mod} ---\n"
                    bundled_code += f"mod_{mod} = types.ModuleType('{mod}')\n"
                    # Simple way to exec and populate module
                    bundled_code += f"exec({repr(m_content)}, mod_{mod}.__dict__)\n"
                    bundled_code += f"sys.modules['oduduwa.stdlib.{mod}'] = mod_{mod}\n"
            
            bundled_code += "\n# --- End of stdlib ---\n\n"
        
        bundled_code += python_code
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(bundled_code)
            
        print(f"Iṣẹ́ parí (Success): A ti kọ fáyìlì sí '{output_path}'")
        
    except Exception as e:
        print(f"Failure during build: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
