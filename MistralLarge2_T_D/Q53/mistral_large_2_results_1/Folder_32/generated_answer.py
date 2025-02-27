import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-zA-Z]', '', s).lower()
    n = 70
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes