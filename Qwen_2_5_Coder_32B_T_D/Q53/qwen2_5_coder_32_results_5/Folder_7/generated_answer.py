import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    letters = re.sub('[^a-z]', '', s)
    palindromes = set()
    length = len(letters)
    for i in range(length):
        for j in range(i + 122, length + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes