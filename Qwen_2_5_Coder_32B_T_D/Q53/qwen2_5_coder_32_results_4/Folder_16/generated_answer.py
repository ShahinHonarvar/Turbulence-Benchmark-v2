import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    letters_only = re.sub('[^a-z]', '', s)
    for i in range(len(letters_only)):
        for j in range(i + 119, len(letters_only) + 1):
            substring = letters_only[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes