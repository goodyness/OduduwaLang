from oduduwa.core.ast import *

class OduduwaTranspiler:
    def __init__(self):
        self.indent_level = 0
        self.output = []
        self.STDLIB = ["iro", "akoko", "iwe", "ayelujara", "json_yoruba", "onka", "isiro"]

    def emit(self, text):
        self.output.append("    " * self.indent_level + text)

    def transpile(self, node):
        self.visit_stmt(node)
        return "\n".join(self.output)

    def visit_stmt(self, node):
        if isinstance(node, Module):
            for stmt in node.body:
                self.visit_stmt(stmt)
        elif isinstance(node, FunctionDef):
            func_name = "__init__" if node.name == "__ibere__" else node.name
            args = ", ".join([a.id for a in node.args])
            self.emit(f"def {func_name}({args}):")
            self.indent_level += 1
            if not node.body:
                self.emit("pass")
            else:
                for stmt in node.body:
                    self.visit_stmt(stmt)
            self.indent_level -= 1
        elif isinstance(node, ClassDef):
            self.emit(f"class {node.name}:")
            self.indent_level += 1
            if not node.body:
                self.emit("pass")
            else:
                for stmt in node.body:
                    self.visit_stmt(stmt)
            self.indent_level -= 1
        elif isinstance(node, TryCatch):
            self.emit("try:")
            self.indent_level += 1
            if not node.body:
                self.emit("pass")
            else:
                for stmt in node.body:
                    self.visit_stmt(stmt)
            self.indent_level -= 1
            
            for handler in node.handlers:
                self.emit("except Exception as e:")
                self.indent_level += 1
                if not handler.body:
                    self.emit("pass")
                else:
                    for stmt in handler.body:
                        self.visit_stmt(stmt)
                self.indent_level -= 1
                
            if node.finalbody:
                self.emit("finally:")
                self.indent_level += 1
                if not node.finalbody:
                    self.emit("pass")
                else:
                    for stmt in node.finalbody:
                        self.visit_stmt(stmt)
                self.indent_level -= 1
        elif isinstance(node, Import):
            imports = []
            for n in node.names:
                if n.id in self.STDLIB:
                    imports.append(f"import oduduwa.stdlib.{n.id} as {n.id}")
                else:
                    imports.append(f"import {n.id}")
            # Ensure proper indentation for all lines
            for imp in imports:
                self.emit(imp)
        elif isinstance(node, ImportFrom):
            mod = node.module.id
            names = ", ".join([n.id for n in node.names])
            if mod in self.STDLIB:
                self.emit(f"from oduduwa.stdlib.{mod} import {names}")
            else:
                self.emit(f"from {mod} import {names}")
        elif isinstance(node, Return):
            if isinstance(node.value, NoneType):
                self.emit("return")
            else:
                val = self.visit_expr(node.value)
                self.emit(f"return {val}")
        elif isinstance(node, If):
            cond = self.visit_expr(node.condition)
            self.emit(f"if {cond}:")
            self.indent_level += 1
            if not node.body:
                self.emit("pass")
            else:
                for stmt in node.body:
                    self.visit_stmt(stmt)
            self.indent_level -= 1
            
            for e_cond, e_body in node.elifs:
                ec = self.visit_expr(e_cond)
                self.emit(f"elif {ec}:")
                self.indent_level += 1
                if not e_body:
                    self.emit("pass")
                else:
                    for stmt in e_body:
                        self.visit_stmt(stmt)
                self.indent_level -= 1

            if node.orelse:
                self.emit("else:")
                self.indent_level += 1
                for stmt in node.orelse:
                    self.visit_stmt(stmt)
                self.indent_level -= 1
        elif isinstance(node, While):
            cond = self.visit_expr(node.condition)
            self.emit(f"while {cond}:")
            self.indent_level += 1
            if not node.body:
                self.emit("pass")
            else:
                for stmt in node.body:
                    self.visit_stmt(stmt)
            self.indent_level -= 1
        elif isinstance(node, ForRange):
            target = node.target.id
            start = self.visit_expr(node.start)
            end = self.visit_expr(node.end)
            # In Python, 'range(start, end)' is exclusive, but in a Yoruba context
            # "from 1 to 5" (láti 1 dé 5) usually implies inclusive (1, 2, 3, 4, 5).
            # We'll make it inclusive by adding + 1 to the end Python-side.
            self.emit(f"for {target} in range({start}, {end} + 1):")
            self.indent_level += 1
            if not node.body:
                self.emit("pass")
            else:
                for stmt in node.body:
                    self.visit_stmt(stmt)
            self.indent_level -= 1
        elif isinstance(node, Assign):
            target = self.visit_expr(node.target)
            value = self.visit_expr(node.value)
            self.emit(f"{target} = {value}")
        elif isinstance(node, Call):
            self.emit(self.visit_expr(node))
        elif isinstance(node, (BinOp, Name, String, Number, Boolean, NoneType)):
            # Bare expression statement, can be safely ignored in Python or emitted as a comment
            pass
        else:
            raise NotImplementedError(f"Statement not implemented: {type(node)}")

    def visit_expr(self, node):
        if isinstance(node, Call):
            func = self.visit_expr(node.func)
            args = ", ".join([self.visit_expr(a) for a in node.args])
            return f"{func}({args})"
        elif isinstance(node, BinOp):
            left = self.visit_expr(node.left)
            right = self.visit_expr(node.right)
            return f"({left} {node.op} {right})"
        elif isinstance(node, Name):
            return node.id
        elif isinstance(node, String):
            return repr(node.s)
        elif isinstance(node, FString):
            return "f" + repr(node.s)
        elif isinstance(node, Number):
            return str(node.n)
        elif isinstance(node, Boolean):
            return "True" if node.b else "False"
        elif isinstance(node, NoneType):
            return "None"
        elif isinstance(node, ListComp):
            elements = ", ".join([self.visit_expr(e) for e in node.elements])
            return f"[{elements}]"
        elif isinstance(node, DictComp):
            pairs = []
            for k, v in zip(node.keys, node.values):
                pairs.append(f"{self.visit_expr(k)}: {self.visit_expr(v)}")
            return "{" + ", ".join(pairs) + "}"
        elif isinstance(node, Attribute):
            value = self.visit_expr(node.value)
            return f"{value}.{node.attr}"
        elif isinstance(node, Return):
            return ""
        else:
            raise NotImplementedError(f"Expression not implemented: {type(node)}")
