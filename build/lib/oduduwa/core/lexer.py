import unicodedata
import re
from enum import Enum, auto

class TokenType(Enum):
    # Keywords
    EGBE = auto()       # class
    ISE = auto()        # def
    PADA = auto()       # return
    TI = auto()         # if
    BIBEEKO = auto()    # else
    SI_TI = auto()      # elif
    FUN = auto()        # for
    NIGBATI = auto()    # while
    GBIYANJU = auto()   # try
    MU_ASISE = auto()   # except
    NI_IPARI = auto()   # finally
    TEJADE = auto()     # print
    SOTITO = auto()     # True
    SEKE = auto()       # False
    OFO = auto()        # None
    LATI = auto()       # from (in ranges)
    DE = auto()         # to (in ranges)
    MU_WOLE = auto()    # import
    
    # Literals & Identifiers
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()
    
    # Operators & Delimiters
    ASSIGN = auto()     # =
    PLUS = auto()       # +
    MINUS = auto()      # -
    MUL = auto()        # *
    DIV = auto()        # /
    LPAREN = auto()     # (
    RPAREN = auto()     # )
    LBRACE = auto()     # {
    RBRACE = auto()     # }
    LBRACKET = auto()   # [
    RBRACKET = auto()   # ]
    COLON = auto()      # :
    COMMA = auto()      # ,
    DOT = auto()        # .
    EQUALS = auto()     # ==
    NOT_EQUALS = auto() # !=
    GREATER = auto()    # >
    LESS = auto()       # <
    GREATER_EQ = auto() # >=
    LESS_EQ = auto()    # <=
    
    # Structure
    INDENT = auto()
    DEDENT = auto()
    NEWLINE = auto()
    EOF = auto()

class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type.name}, {repr(self.value)}, line={self.line}, col={self.column})"

KEYWORDS = {
    "egbe": TokenType.EGBE,
    "ise": TokenType.ISE,
    "pada": TokenType.PADA,
    "ti": TokenType.TI,
    "bibeeko": TokenType.BIBEEKO,
    "si_ti": TokenType.SI_TI,
    "fun": TokenType.FUN,
    "nigbati": TokenType.NIGBATI,
    "gbiyanju": TokenType.GBIYANJU,
    "mu_asise": TokenType.MU_ASISE,
    "ni_ipari": TokenType.NI_IPARI,
    "tejade": TokenType.TEJADE,
    "sotito": TokenType.SOTITO,
    "ooto": TokenType.SOTITO,
    "seke": TokenType.SEKE,
    "iro": TokenType.SEKE,
    "ofo": TokenType.OFO,
    "lati": TokenType.LATI,
    "de": TokenType.DE,
    "mu_wole": TokenType.MU_WOLE,
}

# Regex for token specs
TOKEN_SPECIFICATION = [
    ('NUMBER',     r'\d+(\.\d*)?'),             # Integer or decimal number
    ('STRING',     r'(".*?"|\'.*?\')'),         # String
    ('ID',         r'[^\W\d]\w*'),              # Identifiers (letters + unicode)
    ('EQUALS',     r'=='),
    ('NOT_EQUALS', r'!='),
    ('GREATER_EQ', r'>='),
    ('LESS_EQ',    r'<='),
    ('ASSIGN',     r'='),
    ('GREATER',    r'>'),
    ('LESS',       r'<'),
    ('PLUS',       r'\+'),
    ('MINUS',      r'-'),
    ('MUL',        r'\*'),
    ('DIV',        r'/'),
    ('LPAREN',     r'\('),
    ('RPAREN',     r'\)'),
    ('LBRACE',     r'\{'),
    ('RBRACE',     r'\}'),
    ('LBRACKET',   r'\['),
    ('RBRACKET',   r'\]'),
    ('COLON',      r':'),
    ('COMMA',      r','),
    ('DOT',        r'\.'),
    ('SKIP',       r'[ \t]+'),                  # Skip over spaces and tabs
    ('COMMENT',    r'#.*'),                     # Comments
    ('MISMATCH',   r'.'),                       # Any other character
]

def normalize_yoruba(text):
    """
    Remove diacritics (tone marks) for internal canonical form.
    Example: 'ṣòtító' -> 'sotito'
    """
    if text is None:
        return None
    # Normalize to NFD to separate characters from diacritics
    nfd_form = unicodedata.normalize('NFD', text)
    result = "".join([c for c in nfd_form if unicodedata.category(c) != 'Mn'])
    return result.lower()

class OduduwaLexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
    
    def tokenize(self):
        lines = self.code.split('\n')
        indent_stack = [0]
        paren_level = 0
        
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPECIFICATION)
        get_token = re.compile(tok_regex).match
        
        line_num = 1
        for line in lines:
            stripped = line.strip()
            # Skip empty lines or pure comments to avoid wrong indentations
            if not stripped or stripped.startswith('#'):
                line_num += 1
                continue
            
            # Indentation
            match = re.match(r'^[ \t]*', line)
            indent_str = match.group(0)
            indent_level = indent_str.replace('\t', '    ').count(' ')
            
            if paren_level == 0:
                if indent_level > indent_stack[-1]:
                    indent_stack.append(indent_level)
                    self.tokens.append(Token(TokenType.INDENT, indent_level, line_num, 0))
                else:
                    while indent_level < indent_stack[-1]:
                        indent_stack.pop()
                        self.tokens.append(Token(TokenType.DEDENT, indent_stack[-1], line_num, 0))
                    if indent_level != indent_stack[-1]:
                        raise SyntaxError(f"IndentationError at line {line_num}: unindent does not match any outer level.")
            
            # Content of the line
            pos = len(indent_str)
            end = len(line)
            while pos < end:
                match = get_token(line, pos)
                if not match:
                    raise SyntaxError(f"Unexpected character {line[pos]} at line {line_num}")
                kind = match.lastgroup
                value = match.group(kind)
                column = pos
                pos = match.end()
                
                if kind in ['LPAREN', 'LBRACE', 'LBRACKET']:
                    paren_level += 1
                elif kind in ['RPAREN', 'RBRACE', 'RBRACKET']:
                    paren_level -= 1
                
                if kind in ['SKIP', 'COMMENT']:
                    continue
                elif kind == 'ID':
                    norm_word = normalize_yoruba(value)
                    if norm_word in KEYWORDS:
                        self.tokens.append(Token(KEYWORDS[norm_word], value, line_num, column))
                    else:
                        self.tokens.append(Token(TokenType.IDENTIFIER, value, line_num, column))
                elif kind == 'MISMATCH':
                    raise SyntaxError(f"Unexpected token {value!r} on line {line_num}")
                else:
                    mapped_type = getattr(TokenType, kind, None)
                    if mapped_type:
                        self.tokens.append(Token(mapped_type, value, line_num, column))
            
            if paren_level == 0:        
                self.tokens.append(Token(TokenType.NEWLINE, '\n', line_num, pos))
            line_num += 1
            
        while len(indent_stack) > 1:
            indent_stack.pop()
            self.tokens.append(Token(TokenType.DEDENT, indent_stack[-1], line_num, 0))
            
        self.tokens.append(Token(TokenType.EOF, '', line_num, 0))
        return self.tokens
