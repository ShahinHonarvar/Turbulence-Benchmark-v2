import ast
import re

def create__code(text_specification):
    function_name, arguments = extract_function_name_and_arguments(text_specification)
    _code = f'{function_name}({arguments})'
    tree = ast.parse(_code)
    return _code

def extract_function_name_and_arguments(text_specification):
    pattern = "'(?P<function_name>\\w+)'\\((?P<arguments>.*)\\)"
    match = re.search(pattern, text_specification)
    if match:
        function_name = match.group('function_name')
        arguments = match.group('arguments')
        return (function_name, arguments)
    else:
        raise ValueError('Could not extract function name and arguments from the text specification.')