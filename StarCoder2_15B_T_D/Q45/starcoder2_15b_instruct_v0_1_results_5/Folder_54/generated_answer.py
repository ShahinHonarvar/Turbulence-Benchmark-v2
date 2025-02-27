import re

def palindromes_between_indices(string):
    string = string.lower()
    pattern = re.compile('[a-z]')
    letters = pattern.findall(string)
    palindromes = set()
    for i in range(4, 10):
        for j in range(len(letters) - i + 1):
            substring = letters[j:j + i]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes