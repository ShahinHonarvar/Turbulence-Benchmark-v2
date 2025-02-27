import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = re.sub('[^A-Za-z]', '', s.lower())
    length = len(s)
    for i in range(length):
        for j in range(i + 43, length + 1):
            sub_str = s[i:j]
            if sub_str == sub_str[::-1]:
                palindromes.add(sub_str)
    return palindromes