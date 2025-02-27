import re

def palindrome_of_length_at_least_n(s):
    letters_only = re.sub('[^a-zA-Z]', '', s).lower()
    palindromes = set()
    n = 95
    for i in range(len(letters_only)):
        for j in range(i + n, len(letters_only) + 1):
            substring = letters_only[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes