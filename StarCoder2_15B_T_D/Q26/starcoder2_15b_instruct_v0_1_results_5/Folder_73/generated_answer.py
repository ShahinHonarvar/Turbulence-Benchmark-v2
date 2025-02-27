import re

def create__code(text_specification):
    pattern = "^Write a function called '(?P<function_name>[a-zA-Z0-9_]+)' that takes one argument, a list of integers, and returns the sum of all integers from the given list that are between (?P<start_num>\\d+) and (?P<end_num>\\d+), both inclusive\\. If the given list does not contain such integers, the function should return 0\\.$"
    match = re.match(pattern, text_specification)
    if match:
        function_name = match.group('function_name')
        start_num = int(match.group('start_num'))
        end_num = int(match.group('end_num'))
        _code = f'def {function_name}(nums):'
        _code += '\n    return sum(num for num in nums if start_num <= num <= end_num)'
        return _code
    else:
        raise ValueError('Invalid text specification')