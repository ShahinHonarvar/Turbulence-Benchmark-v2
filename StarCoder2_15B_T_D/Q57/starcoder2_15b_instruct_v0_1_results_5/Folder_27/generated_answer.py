import re
import numpy as np

def create__code(text_specification):
    function_name_pattern = '(?<=function called\\\\s+)\\\\w+'
    argument_name_pattern = '(?<=the\\\\s+)\\\\w+(?=\\\\s+argument)'
    desired_sum_pattern = '(?<=the\\\\s+sum\\\\s+of\\\\s+all\\\\s+integers\\\\s+in\\\\s+each\\\\s+submatrix\\\\s+equals\\\\s+)\\\\d+'
    function_name = re.search(function_name_pattern, text_specification).group(0)
    argument_name = re.search(argument_name_pattern, text_specification).group(0)
    desired_sum = int(re.search(desired_sum_pattern, text_specification).group(0))
    _code = f'def {function_name}({argument_name}):'
    _code += '    submatrices = []'
    _code += '    for i in range(len({argument_name}) - 1):'
    _code += '        for j in range(len({argument_name}[0]) - 1):'
    _code += '            submatrix = {argument_name}[i:i+2, j:j+2]'
    _code += '            if submatrix.sum() == {desired_sum}:'
    _code += '                submatrices.append(submatrix)'
    _code += '    return submatrices'
    return _code