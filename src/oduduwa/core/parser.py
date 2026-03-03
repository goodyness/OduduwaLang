from .ast import *
from .lexer import TokenType, Token

class ParserError(Exception):
    pass

class OduduwaParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return self.tokens[-1] # EOF

    def advance(self):
        tok = self.current()
        self.pos += 1
        return tok

    def match(self, *types):
        if self.current().type in types:
            return self.advance()
        return None

    def expect(self, tok_type, expected_msg=""):
        tok = self.match(tok_type)
        if not tok:
            raise ParserError(f"Expected {tok_type.name} {expected_msg}, got {self.current().type.name} at line {self.current().line}")
        return tok

    def parse(self):
        body = []
        while self.current().type != TokenType.EOF:
            if self.current().type == TokenType.NEWLINE:
                self.advance()
                continue
            stmt = self.statement()
            if stmt:
                body.append(stmt)
        return Module(body)

    def statement(self):
        tok = self.current()
        if tok.type == TokenType.ISE:
            return self.function_def()
        elif tok.type == TokenType.EGBE:
            return self.class_def()
        elif tok.type == TokenType.GBIYANJU:
            return self.try_statement()
        elif tok.type == TokenType.MU_WOLE:
            return self.import_statement()
        elif tok.type == TokenType.LATI:
            return self.import_from_statement()
        elif tok.type == TokenType.TI:
            return self.if_statement()
        elif tok.type == TokenType.NIGBATI:
            return self.while_statement()
        elif tok.type == TokenType.FUN:
            return self.for_statement()
        elif tok.type == TokenType.PADA:
            self.advance()
            val = self.expression() if self.current().type != TokenType.NEWLINE else NoneType()
            self.expect(TokenType.NEWLINE)
            return Return(val)
        # Expression or Assignment statement
        expr = self.expression()
        if self.match(TokenType.ASSIGN):
            value = self.expression()
            self.expect(TokenType.NEWLINE)
            return Assign(expr, value)
            
        self.expect(TokenType.NEWLINE, "after expression")
        return expr

    def function_def(self):
        self.expect(TokenType.ISE)
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.LPAREN)
        args = []
        if self.current().type != TokenType.RPAREN:
            args.append(Name(self.expect(TokenType.IDENTIFIER).value))
            while self.match(TokenType.COMMA):
                args.append(Name(self.expect(TokenType.IDENTIFIER).value))
        self.expect(TokenType.RPAREN)
        self.expect(TokenType.COLON)
        self.expect(TokenType.NEWLINE)
        body = self.block()
        return FunctionDef(name, args, body)

    def class_def(self):
        self.expect(TokenType.EGBE)
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.COLON)
        self.expect(TokenType.NEWLINE)
        body = self.block()
        return ClassDef(name, body)

    def try_statement(self):
        self.expect(TokenType.GBIYANJU)
        self.expect(TokenType.COLON)
        self.expect(TokenType.NEWLINE)
        body = self.block()
        
        handlers = []
        orelse = []
        finalbody = []
        
        while self.current().type == TokenType.NEWLINE:
            self.advance()
            
        while self.current().type == TokenType.MU_ASISE:
            self.expect(TokenType.MU_ASISE)
            self.expect(TokenType.COLON)
            self.expect(TokenType.NEWLINE)
            h_body = self.block()
            handlers.append(ExceptHandler(None, h_body))
            
            while self.current().type == TokenType.NEWLINE:
                self.advance()
                
        if self.current().type == TokenType.NI_IPARI:
            self.expect(TokenType.NI_IPARI)
            self.expect(TokenType.COLON)
            self.expect(TokenType.NEWLINE)
            finalbody = self.block()
            
        return TryCatch(body, handlers, orelse, finalbody)

    def while_statement(self):
        self.expect(TokenType.NIGBATI)
        condition = self.expression()
        self.expect(TokenType.COLON)
        self.expect(TokenType.NEWLINE)
        body = self.block()
        return While(condition, body)

    def import_statement(self):
        self.expect(TokenType.MU_WOLE)
        names = []
        names.append(Name(self.expect(TokenType.IDENTIFIER).value))
        while self.current().type == TokenType.COMMA:
            self.advance()
            names.append(Name(self.expect(TokenType.IDENTIFIER).value))
        self.expect(TokenType.NEWLINE)
        return Import(names)

    def import_from_statement(self):
        self.expect(TokenType.LATI)
        module = Name(self.expect(TokenType.IDENTIFIER).value)
        self.expect(TokenType.MU_WOLE)
        names = []
        names.append(Name(self.expect(TokenType.IDENTIFIER).value))
        while self.current().type == TokenType.COMMA:
            self.advance()
            names.append(Name(self.expect(TokenType.IDENTIFIER).value))
        self.expect(TokenType.NEWLINE)
        return ImportFrom(module, names)

    def for_statement(self):
        # fún i láti 1 dé 5:
        self.expect(TokenType.FUN)
        target = Name(self.expect(TokenType.IDENTIFIER).value)
        self.expect(TokenType.LATI)
        start = self.expression()
        self.expect(TokenType.DE)
        end = self.expression()
        self.expect(TokenType.COLON)
        self.expect(TokenType.NEWLINE)
        body = self.block()
        return ForRange(target, start, end, body)

    def if_statement(self):
        self.expect(TokenType.TI)
        condition = self.expression()
        self.expect(TokenType.COLON)
        self.expect(TokenType.NEWLINE)
        body = self.block()
        
        orelse = []
        # Skip optional blank lines
        while self.current().type == TokenType.NEWLINE:
            self.advance()
            
        if self.current().type == TokenType.BIBEEKO:
            self.expect(TokenType.BIBEEKO)
            self.expect(TokenType.COLON)
            self.expect(TokenType.NEWLINE)
            orelse = self.block()
            
        return If(condition, body, orelse)

    def assignment(self):
        target = Name(self.expect(TokenType.IDENTIFIER).value)
        self.expect(TokenType.ASSIGN)
        value = self.expression()
        self.expect(TokenType.NEWLINE)
        return Assign(target, value)

    def block(self):
        self.expect(TokenType.INDENT)
        stmts = []
        while self.current().type not in (TokenType.DEDENT, TokenType.EOF):
            if self.current().type == TokenType.NEWLINE:
                self.advance()
                continue
            stmts.append(self.statement())
        self.expect(TokenType.DEDENT)
        return stmts

    def expression(self):
        return self.comparison()
        
    def comparison(self):
        left = self.addition()
        if self.current().type in (TokenType.EQUALS, TokenType.NOT_EQUALS, TokenType.GREATER, TokenType.LESS, TokenType.GREATER_EQ, TokenType.LESS_EQ):
            op = self.advance().value
            right = self.addition()
            return BinOp(left, op, right)
        return left

    def addition(self):
        left = self.multiplication()
        while self.current().type in (TokenType.PLUS, TokenType.MINUS):
            op = self.advance().value
            right = self.multiplication()
            left = BinOp(left, op, right)
        return left

    def multiplication(self):
        left = self.primary()
        while self.current().type in (TokenType.MUL, TokenType.DIV):
            op = self.advance().value
            right = self.primary()
            left = BinOp(left, op, right)
        return left

    def primary(self):
        tok = self.advance()
        node = None
        if tok.type == TokenType.NUMBER:
            node = Number(tok.value)
        elif tok.type == TokenType.STRING:
            node = String(tok.value[1:-1]) # Strip quotes
        elif tok.type == TokenType.SOTITO:
            node = Boolean(True)
        elif tok.type == TokenType.SEKE:
            node = Boolean(False)
        elif tok.type == TokenType.OFO:
            node = NoneType()
        elif tok.type == TokenType.TEJADE:
            self.expect(TokenType.LPAREN)
            args = []
            if self.current().type != TokenType.RPAREN:
                args.append(self.expression())
                while self.match(TokenType.COMMA):
                    args.append(self.expression())
            self.expect(TokenType.RPAREN)
            node = Call(Name("print"), args)
        elif tok.type == TokenType.IDENTIFIER:
            node = Name(tok.value)
        elif tok.type == TokenType.LPAREN:
            node = self.expression()
            self.expect(TokenType.RPAREN)
        elif tok.type == TokenType.LBRACKET:
            elements = []
            while self.current().type == TokenType.NEWLINE:
                self.advance()
            if self.current().type != TokenType.RBRACKET:
                elements.append(self.expression())
                while self.current().type == TokenType.NEWLINE:
                    self.advance()
                while self.match(TokenType.COMMA):
                    while self.current().type == TokenType.NEWLINE:
                        self.advance()
                    elements.append(self.expression())
                    while self.current().type == TokenType.NEWLINE:
                        self.advance()
            self.expect(TokenType.RBRACKET)
            node = ListComp(elements)
        elif tok.type == TokenType.LBRACE:
            keys = []
            values = []
            while self.current().type == TokenType.NEWLINE:
                self.advance()
            if self.current().type != TokenType.RBRACE:
                keys.append(self.expression())
                self.expect(TokenType.COLON)
                values.append(self.expression())
                while self.current().type == TokenType.NEWLINE:
                    self.advance()
                while self.match(TokenType.COMMA):
                    while self.current().type == TokenType.NEWLINE:
                        self.advance()
                    keys.append(self.expression())
                    self.expect(TokenType.COLON)
                    values.append(self.expression())
                    while self.current().type == TokenType.NEWLINE:
                        self.advance()
            self.expect(TokenType.RBRACE)
            node = DictComp(keys, values)
        else:
            raise ParserError(f"Unexpected token {tok.type.name} at line {tok.line}")

        # Handle trailing operations (calls, attributes)
        while True:
            if self.match(TokenType.LPAREN):
                args = []
                if self.current().type != TokenType.RPAREN:
                    args.append(self.expression())
                    while self.match(TokenType.COMMA):
                        args.append(self.expression())
                self.expect(TokenType.RPAREN)
                node = Call(node, args)
            elif self.match(TokenType.DOT):
                attr_name = self.expect(TokenType.IDENTIFIER).value
                node = Attribute(node, attr_name)
            else:
                break
                
        return node
