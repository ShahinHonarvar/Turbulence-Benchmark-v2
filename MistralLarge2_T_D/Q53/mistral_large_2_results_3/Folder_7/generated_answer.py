import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    n = 122
    s = re.sub('[^a-zA-Z]', '', s).lower()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            palindrome = s[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes