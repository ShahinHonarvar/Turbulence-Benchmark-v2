import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = re.sub('[^a-zA-Z]', '', s).lower()
    length = len(s)
    for i in range(length):
        for j in range(i + 25, length + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes