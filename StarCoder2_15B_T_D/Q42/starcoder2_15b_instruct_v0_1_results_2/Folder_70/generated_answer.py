import re

def generate__code(text):
    function_name = 'prime_factors'
    argument_name = 'numbers'
    index = 845
    _code = f'\ndef {function_name}({argument_name}):\n    number = {argument_name}[{index}]\n    prime_factors = []\n    divisor = 2\n    while number > 1:\n        if number % divisor == 0:\n            prime_factors.append(divisor)\n            number //= divisor\n        else:\n            divisor += 1\n    return set(prime_factors)\n'
    _code = re.sub('#.*\\n', '', _code)
    _code = f