import re

def palindromes_between_indices(s):
    pattern = re.compile('[a-zA-Z]')
    letters = pattern.findall(s)
    palindromes = set()
    for i in range(1, 5):
        for j in range(i + 3, len(letters) + 1):
            palindrome = ''.join(letters[i:j])
            if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes