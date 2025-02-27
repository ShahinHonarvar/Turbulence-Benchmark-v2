import ast

def generate__code(text_specification):
    try:
        specification_ast = ast.parse(text_specification)
        function_name = specification_ast.body[0].name
        args = [arg.arg for arg in specification_ast.body[0].args.args]
        _code = f'def {function_name}({', '.join(args)}):    pass'
        return _code
    except Exception as e:
        raise ValueError(f'Invalid text specification: {text_specification}') from e