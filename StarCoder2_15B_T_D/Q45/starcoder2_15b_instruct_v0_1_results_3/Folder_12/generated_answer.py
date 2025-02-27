import re

def palindromes_between_indices(string):
    letters = re.findall('[a-z]', string[3:9].lower())
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            palindrome = ''.join(letters[i:i + length])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes