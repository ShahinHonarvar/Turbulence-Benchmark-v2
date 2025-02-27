import re
import code

def create__code(text_specification):
    pattern = '<(\\\\w+) that takes one argument, a list of integers, and returns the list of all even integers from index 50 to index 92, both exclusive. If no even integers exist in the specified range, the function should return an empty list.>'
    match = re.search(pattern, text_specification)
    if match:
        function_name = match.group(1)
        function_signature = f'def {function_name}(numbers):'
        function_body = '\n    even_numbers = []\n    for i in range(50, 92):\n        if numbers[i] % 2 == 0:\n            even_numbers.append(numbers[i])\n\n    return even_numbers\n'
        _code = code.FunctionCode(function_name, function_signature, function_body).code
        return _code
    else:
        raise ValueError('Invalid text specification')