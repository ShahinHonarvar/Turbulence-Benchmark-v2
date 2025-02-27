import re

def create__code(text_specification):
    function_name = re.findall("'(.*?)'", text_specification)[0]
    arguments = re.findall('\\((.*?)\\)', text_specification)[0]
    function_logic = re.findall('\\n(.*?)\\n', text_specification, re.DOTALL)[0]
    _code = f'def {function_name}({arguments}):\n'
    _code += f'    {function_logic}\n'
    _code += f'    return '
    return _code