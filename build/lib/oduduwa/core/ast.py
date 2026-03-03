class ASTNode:
    pass

class Module(ASTNode):
    def __init__(self, body):
        self.body = body # List of statements

class ClassDef(ASTNode):
    def __init__(self, name, body):
        self.name = name
        self.body = body # List of statements

class FunctionDef(ASTNode):
    def __init__(self, name, args, body):
        self.name = name
        self.args = args # List of Names
        self.body = body # List of statements

class Return(ASTNode):
    def __init__(self, value):
        self.value = value

class If(ASTNode):
    def __init__(self, condition, body, orelse):
        self.condition = condition
        self.body = body # List of statements
        self.orelse = orelse # List of statements

class While(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body # List of statements

class TryCatch(ASTNode):
    def __init__(self, body, handlers, orelse, finalbody):
        self.body = body           # List of statements
        self.handlers = handlers   # List of ExceptHandler nodes (we can simplify to just body for now)
        self.orelse = orelse       # List of statements (else)
        self.finalbody = finalbody # List of statements (finally)

class ExceptHandler(ASTNode):
    def __init__(self, name, body):
        self.name = name           # String (alias) or None
        self.body = body           # List of statements

class Import(ASTNode):
    def __init__(self, names):
        self.names = names # List of Name nodes

class ImportFrom(ASTNode):
    def __init__(self, module, names):
        self.module = module # Name node
        self.names = names   # List of Name nodes

class ForRange(ASTNode):
    def __init__(self, target, start, end, body):
        self.target = target # Name
        self.start = start   # Expression
        self.end = end       # Expression
        self.body = body     # List of statements

class Attribute(ASTNode):
    def __init__(self, value, attr):
        self.value = value # Expression
        self.attr = attr   # String (name)

class ListComp(ASTNode):
    def __init__(self, elements):
        self.elements = elements # List of Expressions

class DictComp(ASTNode):
    def __init__(self, keys, values):
        self.keys = keys     # List of Expressions
        self.values = values # List of Expressions

class Assign(ASTNode):
    def __init__(self, target, value):
        self.target = target
        self.value = value

class Call(ASTNode):
    def __init__(self, func, args):
        self.func = func # Expression
        self.args = args # List of Expressions

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Name(ASTNode):
    def __init__(self, id):
        self.id = id

class String(ASTNode):
    def __init__(self, s):
        self.s = s

class Number(ASTNode):
    def __init__(self, n):
        self.n = n

class Boolean(ASTNode):
    def __init__(self, b):
        self.b = b

class NoneType(ASTNode):
    pass
