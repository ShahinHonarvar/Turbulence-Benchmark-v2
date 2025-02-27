import re

def palindrome_of_length_n(s):
    s = s.lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for i in range(len(s) - 112):
        substring = s[i:i + 113]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes