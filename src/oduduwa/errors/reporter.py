import sys
import traceback
from oduduwa.core.parser import ParserError

# Map Python exceptions to Yoruba
EXCEPTION_MAP = {
    "SyntaxError": "Aṣiṣe Gírámà (Syntax Error)",
    "NameError": "Aṣiṣe Orukọ (Name Error)",
    "TypeError": "Aṣiṣe Ẹyà (Type Error)",
    "ZeroDivisionError": "Aṣiṣe Pín-Pín pẹlu Ódo (Divide by Zero)",
    "IndexError": "Aṣiṣe Atọka (Index Out of Bounds)",
    "KeyError": "Aṣiṣe Kókó (Key Not Found)",
    "ValueError": "Aṣiṣe Iye (Value Error)",
    "ParserError": "Aṣiṣe Ìtumọ̀ Gírámà (Parser Error)",
    "AttributeError": "Aṣiṣe Àfihàn (Attribute Error)",
    "ImportError": "Aṣiṣe Ìgbéwọlé (Import Error)",
    "ModuleNotFoundError": "A kò rí Ẹka (Module Not Found)",
    "FileNotFoundError": "A kò rí Fáìlì (File Not Found)",
    "Exception": "Aṣiṣe Gbogbogbò (General Error)"
}

def translate_exception(exc_type_name):
    return EXCEPTION_MAP.get(exc_type_name, f"Aṣiṣe ({exc_type_name})")

def handle_exception(exc_type, exc_value, exc_traceback, source_lines=None):
    """
    Format a Python exception into a beautifully formatted Yoruba stack trace.
    """
    print("\n" + "="*50)
    print("❌ IPADE AṢIṢE (ERROR ENCOUNTERED) ❌")
    print("="*50)
    
    exc_name = exc_type.__name__
    yoruba_name = translate_exception(exc_name)
    
    print(f"\nIru Aṣiṣe (Error Type): {yoruba_name}")
    print(f"Ipilẹ Aṣiṣe (Details): {exc_value}")
    
    # Extract line number if present
    line_num = -1
    
    # Specialized handling for ParserError
    if exc_name == "ParserError":
        # Extract "at line X" from parser error message if present
        msg = str(exc_value)
        if "at line " in msg:
            try:
                line_part = msg.split("at line ")[1]
                line_num = int(''.join(filter(str.isdigit, line_part)))
            except:
                pass
                
    # Otherwise check standard traceback
    if line_num == -1 and exc_traceback:
        # Get the innermost traceback frame that refers to our code
        # Since exec generates dynamic frames, it might show up as '<string>'
        for frame in reversed(traceback.extract_tb(exc_traceback)):
            if frame.filename == '<string>' or frame.filename.endswith('.odu'):
                line_num = frame.lineno
                print(f"\nA ṣẹlẹ ni ila (Occurred at line): {line_num}")
                break
                
    # Print the source code context if available
    if line_num > 0 and source_lines and line_num <= len(source_lines):
        print("\nÀyè tí aṣiṣe ti sẹlẹ (Context):")
        start = max(1, line_num - 1)
        end = min(len(source_lines), line_num + 1)
        for i in range(start, end + 1):
            prefix = "--> " if i == line_num else "    "
            print(f"{prefix}{i} | {source_lines[i-1]}")
            
    print("\nẸjọwọ ṣe atunṣe ki o tun fi ranṣẹ (Please fix and try again).")
    print("="*50 + "\n")
