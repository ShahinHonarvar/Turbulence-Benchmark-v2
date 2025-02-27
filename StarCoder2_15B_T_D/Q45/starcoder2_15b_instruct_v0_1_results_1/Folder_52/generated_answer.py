import re

def palindromes_between_indices(text):
    palindromes = set()
    pattern = '[a-zA-Z]'
    letters = re.findall(pattern, text)
    for i in range(len(letters) - 7):
        for j in range(i + 6, len(letters)):
            substring = ''.join(letters[i:j + 1])
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes