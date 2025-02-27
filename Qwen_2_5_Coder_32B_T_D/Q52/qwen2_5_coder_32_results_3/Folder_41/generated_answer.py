import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    s = re.sub('[^a-z]', '', s)
    for i in range(len(s) - 59):
        substring = s[i:i + 60]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes