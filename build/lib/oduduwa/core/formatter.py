import os
import sys

def format_file(filepath):
    """
    ṣè_ètò (Format) an OduduwaLang file.
    Because rebuilding the exact source from AST is extremely complex conceptually
    we will build a simple block indentation formatter using the generic Oduduwa token rules.
    """
    if not os.path.exists(filepath):
        print(f"Aṣiṣe (Error): Kò rí fáyìlì '{filepath}' (File not found).")
        sys.exit(1)
        
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    formatted = []
    current_indent = 0
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            formatted.append("")
            continue
            
        # Very basic bracket/colon block tracking
        # If it's a dedent indicator like a closing bracket/brace, decrease indent BEFORE printing
        if stripped.startswith('mu_asise') or stripped.startswith('ni_ipari'):
            if current_indent > 0: current_indent -= 1
            
        formatted.append(("    " * current_indent) + stripped)
        
        # Increase indent AFTER a block starter
        if stripped.endswith(':'):
            current_indent += 1
            
        # If it's `mu_asise` it started a new block but closed the try block. 
        if stripped.startswith('mu_asise'):
            current_indent += 1

    final_code = "\n".join(formatted) + "\n"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_code)
        
    print(f"✨ A ti ṣè_ètò fáìlì '{(filepath)}' (File has been formatted).")
