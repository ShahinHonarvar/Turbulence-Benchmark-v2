import re

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string)
    palindromes = set()
    for i in range(2, 7):
        for j in range(i + 1, 8):
            if i + j < 6:
                continue
            substring = ''.join(letters[i:j + 1])
            reversed_substring = substring[::-1]
            if substring.lower() == reversed_substring.lower():
                palindromes.add(substring)
    return palindromes