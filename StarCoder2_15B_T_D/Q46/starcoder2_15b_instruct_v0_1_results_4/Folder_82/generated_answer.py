import re
import textwrap

def create__code(text_specification):
    text_specification = re.search('<(.*)>', text_specification).group(1)
    function_name, arguments, return_value = text_specification.split(' ')
    arguments = arguments.strip('()')
    return_value = return_value.strip('.')
    _code = f'def {function_name}({arguments}):'
    _code += textwrap.indent('return gcf([arg[67], arg[84], arg[13]])', '   ')
    _code = f