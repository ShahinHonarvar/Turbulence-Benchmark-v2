import re

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string)
    palindromes = set()
    for i in range(1, len(letters) - 1):
        for j in range(i + 5, len(letters)):
            palindrome = ''.join(letters[i:j])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes