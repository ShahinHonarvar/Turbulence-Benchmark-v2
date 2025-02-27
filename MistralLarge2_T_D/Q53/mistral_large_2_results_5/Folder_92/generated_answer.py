import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = re.sub('[^A-Za-z]', '', s).lower()
    length = len(s)
    for i in range(length):
        for j in range(i + 10, length + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes