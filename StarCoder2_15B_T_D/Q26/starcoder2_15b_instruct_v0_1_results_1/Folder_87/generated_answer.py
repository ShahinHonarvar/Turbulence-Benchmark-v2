import re

def create__code(text_specification):
    pattern = re.compile("^Write a function called '(?P<function_name>\\w+)' that takes one argument, a list of integers, and returns the sum of all integers from the given list that are between 60 and 90, both inclusive\\. If the given list does not contain such integers, the function should return 0\\.$")
    match = pattern.match(text_specification)
    if match:
        function_name = match.group('function_name')
        _code = f'def {function_name}(numbers):'
        _code += '\n    total = 0'
        _code += '\n    for num in numbers:'
        _code += '\n        if 60 <= num <= 90:'
        _code += '\n            total += num'
        _code += '\n    return total'
        return _code
    else:
        raise ValueError('Invalid text specification')