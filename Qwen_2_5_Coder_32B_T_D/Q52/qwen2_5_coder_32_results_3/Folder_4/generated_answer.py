import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s).lower()
    palindromes = set()
    for i in range(len(s) - 14):
        substr = s[i:i + 15]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes