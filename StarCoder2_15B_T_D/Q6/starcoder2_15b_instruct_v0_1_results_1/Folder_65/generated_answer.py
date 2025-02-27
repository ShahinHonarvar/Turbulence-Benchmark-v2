import re

def generate__code(text_specification):
    function_name_pattern = '^<(?P<function_name>\\w+)\\((?P<argument_list>.*)\\)>'
    match = re.match(function_name_pattern, text_specification)
    if match:
        function_name = match.group('function_name')
        argument_list = match.group('argument_list')
        _code = f'def {function_name}({argument_list}):\n    pass'
        return f