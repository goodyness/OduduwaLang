import sys
import os
from oduduwa.core.lexer import OduduwaLexer
from oduduwa.core.parser import OduduwaParser
from oduduwa.core.transpiler import OduduwaTranspiler
from oduduwa.errors.reporter import handle_exception
import oduduwa.stdlib.iro as iro

def print_help():
    print("\n" + "="*45)
    print(" IRANLỌWỌ (HELP) - OduduwaLang")
    print("="*45)
    print(" - Tẹ 'jade()' lati kuro (Type 'jade()' to exit)")
    print(" - Tẹ 'pare' lati pa oju iwe rẹ (Type 'pare' to clear screen)")
    print(" - Tẹ 'iranlowo' lati ri eyi (Type 'iranlowo' for help)")
    print("\nAwọn Kókó Ọ̀rọ̀ (Keywords):")
    print("  ise       : def (function definition)")
    print("  pada      : return")
    print("  ti        : if")
    print("  si_ti     : elif")
    print("  bibeeko   : else")
    print("  fun       : for (loops)")
    print("  nigbati   : while (loops)")
    print("  tejade    : print")
    print("  sotito/ooto : True")
    print("  seke/iro  : False")
    print("\nApeere (Examples):")
    print("  odu> tejade(\"Bawo ni?\")")
    print("  odu> oruko = \"Ade\"")
    print("="*45 + "\n")

def start_repl():
    print("=======================================")
    print(" OduduwaLang REPL v0.1.0")
    print(" Tẹ 'iranlowo' (tabi 'help') fun itọsọna.")
    print(" Tẹ 'jade()' lati kuro (Type 'jade()' to exit)")
    print("=======================================")
    
    env_globals = globals().copy()
    env_globals['iro'] = iro
    
    while True:
        try:
            # Yoruba prompt
            line = input("odu> ")
            
            if not line.strip():
                continue
                
            command = line.strip().lower()
            if command in ["jade()", "jade", "exit", "exit()", "quit", "quit()"]:
                print("O dabo! (Goodbye!)")
                break
                
            if command in ["iranlowo", "iranlowo()", "help", "help()"]:
                print_help()
                continue
                
            if command in ["pare", "pare()", "clear", "clear()", "cls"]:
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
                
            # Lex -> Parse -> Transpile
            lexer = OduduwaLexer(line)
            tokens = lexer.tokenize()
            
            parser = OduduwaParser(tokens)
            ast = parser.parse()
            
            transpiler = OduduwaTranspiler()
            python_code = transpiler.transpile(ast)
            
            # Execute
            try:
                exec(python_code, env_globals)
                
            except Exception as e:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                handle_exception(exc_type, exc_value, exc_traceback, [line])
                print("💡 Akiyesi: Tẹ 'iranlowo' tabi 'help' fun itọsọna. (Type 'help' for instructions.)\n")
                
        except EOFError:
            print("\nO dabo!")
            break
        except KeyboardInterrupt:
            print("\n(Ti da duro - Interrupted)")
            continue
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            handle_exception(exc_type, exc_value, exc_traceback, [line])
            print("💡 Akiyesi: Tẹ 'iranlowo' tabi 'help' fun itọsọna. (Type 'help' for instructions.)\n")
