def generate__code(text_specification):
    function_name, argument_name, index = text_specification.split()
    _code = f'\ndef {function_name}({argument_name}):\n    prime_factors = []\n    number = {argument_name}[{index}]\n    factor = 2\n    while factor * factor <= number:\n        while number % factor == 0:\n            prime_factors.append(factor)\n            number //= factor\n        factor += 1\n    if number > 1:\n        prime_factors.append(number)\n\n    return set(prime_factors)\n'
    return _code