import re

def create__code(text_specification):
    function_name, argument_name, indices = re.findall("'(.*?)'|\\\\[(.*?)\\\\]", text_specification)
    indices = [int(index) for index in indices.split(',')]
    _code = f'\ndef {function_name}({argument_name}):\n    gcf = 1\n    for index in {indices}:\n        gcf = gcf_of_two_nums({argument_name}[index], gcf)\n    return gcf\n'
    return _code