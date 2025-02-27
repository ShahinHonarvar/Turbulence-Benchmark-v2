import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 9
    palindromes = set()
    words = re.findall('\\\\b[a-z]+\\\\b', s)
    for word in words:
        length = len(word)
        if length >= n:
            for i in range(length):
                for j in range(i + n, length + 1):
                    substring = word[i:j]
                    if substring == substring[::-1]:
                        palindromes.add(substring)
    return palindromes