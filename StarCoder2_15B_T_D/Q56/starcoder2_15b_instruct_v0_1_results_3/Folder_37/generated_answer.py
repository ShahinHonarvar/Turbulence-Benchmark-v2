import re

def create__code(text_specification):
    pattern = '\\\\<(.+)\\\\>'
    match = re.search(pattern, text_specification)
    if match:
        function_name, arguments = match.group(1).split('(')
        function_name = function_name.strip()
        arguments = arguments.strip(')')
        _code = f'def {function_name}({arguments}):    pass'
        return _code
    else:
        return ''