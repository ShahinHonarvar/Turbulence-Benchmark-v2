import re

def palindromes_of_specific_lengths(string):
    substring = string[:6]
    pattern = re.compile('[a-zA-Z]{3,5}')
    palindromes = set()
    for i in range(len(substring) - 5):
        for j in range(i + 3, min(i + 6, len(substring))):
            palindrome = substring[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes