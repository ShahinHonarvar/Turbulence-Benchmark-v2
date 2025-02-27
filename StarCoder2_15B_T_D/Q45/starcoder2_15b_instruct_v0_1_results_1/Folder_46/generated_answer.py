import re

def palindromes_between_indices(text):
    pattern = re.compile('[a-zA-Z]')
    letters = pattern.findall(text)
    palindromes = set()
    for i in range(len(letters) - 5):
        for j in range(i + 6, len(letters) + 1):
            palindrome = ''.join(letters[i:j])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes