import re

def generate__code(text_specification):
    pattern = "^Write a function called '(?P<function_name>[a-zA-Z0-9_]+)' that takes one argument, a list of integers, and returns the sum of all integers divisible by either -94 or -95 from index 50 to index 92, both inclusive\\\\. If no such integers exist in the specified range, the function should return 0\\\\.$"
    match = re.match(pattern, text_specification)
    if match:
        function_name = match.group('function_name')
        _code = f'def {function_name}(nums):'
        _code += '    sum = 0'
        _code += '    for i in range(50, 93):'
        _code += '        if nums[i] % -94 == 0 or nums[i] % -95 == 0:'
        _code += '            sum += nums[i]'
        _code += '    return sum'
        return _code
    else:
        raise ValueError('Invalid text specification')