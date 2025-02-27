import re
import re

def create__code(text_specification):
    function_name_pattern = "'(\\\\w+)'"
    argument_name_pattern = "'(\\\\w+)'"
    function_name = re.search(function_name_pattern, text_specification).group(1)
    argument_name = re.search(argument_name_pattern, text_specification).group(1)
    _code = f'\\\n\ndef {function_name}({argument_name}):\n    pattern = r"(?=([^\\]{127}))"\n    return re.findall(pattern, {argument_name})\n'
    return _code