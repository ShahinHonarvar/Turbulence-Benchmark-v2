import re

def palindromes_between_indices(string):
    palindromes = set()
    pattern = re.compile('[a-zA-Z]')
    letters = pattern.findall(string)
    for i in range(len(letters) - 3):
        for j in range(i + 3, len(letters) + 1):
            palindrome = ''.join(letters[i:j])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes