import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 38):
        substring = re.sub('[^a-z]', '', s[i:i + 39])
        if len(substring) == 39 and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes