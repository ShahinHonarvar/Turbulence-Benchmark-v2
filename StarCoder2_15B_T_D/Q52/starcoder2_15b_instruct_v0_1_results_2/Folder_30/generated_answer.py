import re

def create__code(text_specification):
    pattern = "^Write a function called '(.*?)' that takes one argument, a string, and returns the set of all palindromes of the length equal to 94, where each palindrome is a substring of the given string\\. Each palindrome should only consist of English letters\\. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set\\. The function should find the palindromes in a case-insensitive manner\\.$"
    match = re.match(pattern, text_specification)
    if match:
        function_name = match.group(1)
        _code = f'def {function_name}(string):\n    string = string.lower()\n    palindromes = set()\n    for i in range(len(string) - 94 + 1):\n        substring = string[i:i+94]\n        if substring == substring[::-1]:\n            palindromes.add(substring)\n\n    return palindromes'
        return _code
    else:
        raise ValueError('Invalid text specification')