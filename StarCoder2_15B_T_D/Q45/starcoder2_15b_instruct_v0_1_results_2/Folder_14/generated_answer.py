import re

def palindromes_between_indices(s):
    pattern = '[a-z]'
    letters = re.findall(pattern, s)
    palindromes = set()
    for i in range(4, len(letters) - 5):
        for j in range(i + 3, len(letters) - 1):
            palindrome = ''.join(letters[i:j + 1])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes