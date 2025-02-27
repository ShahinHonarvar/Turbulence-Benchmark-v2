import ast

def generate__code(text):
    spec = ast.parse(text)
    func_name = spec.body[0].name
    args = spec.body[0].args.args
    return_stmt = spec.body[0].body[0]
    _code = f'def {func_name}({', '.join((arg.arg for arg in args))}):\n'
    _code += f'    return {ast.dump(return_stmt)[7:-1]}\n'
    return _code