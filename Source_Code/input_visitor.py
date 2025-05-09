import ast


class InputFunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.found_input = False

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if node.func.id in ('input', 'raw_input'):
                self.found_input = True

        elif isinstance(node.func, ast.Attribute):
            attr = node.func
            if isinstance(attr.value, ast.Attribute):
                if (isinstance(attr.value.value, ast.Name) and
                        attr.value.value.id == 'sys' and
                        attr.value.attr == 'stdin'):
                    if attr.attr in ('read', 'readline', 'readlines'):
                        self.found_input = True

        elif isinstance(node.func, ast.Attribute):
            if (isinstance(node.func.value, ast.Name) and
                    node.func.value.id == 'fileinput' and
                    node.func.attr == 'input'):
                self.found_input = True

        elif isinstance(node.func, ast.Name) and node.func.id == 'open':
            if len(node.args) >= 1:
                arg0 = node.args[0]
                if isinstance(arg0, ast.Str) and arg0.s == '/dev/stdin':
                    self.found_input = True

        self.generic_visit(node)