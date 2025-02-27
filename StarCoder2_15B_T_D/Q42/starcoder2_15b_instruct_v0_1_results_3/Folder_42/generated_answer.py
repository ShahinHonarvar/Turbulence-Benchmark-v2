import ast

def create__code(text_specification):
    spec_tree = ast.parse(text_specification)
    function_name = spec_tree.body[0].name
    argument_name = spec_tree.body[0].args.args[0].arg
    index = spec_tree.body[0].body[0].value.n
    _code = f'\ndef {function_name}({argument_name}):\n    return set(prime_factors({argument_name}[{index}]))\n'
    return _code