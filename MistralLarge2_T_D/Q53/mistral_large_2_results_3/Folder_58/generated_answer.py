import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    n = 147
    s = re.sub('[^a-zA-Z]', '', s).lower()
    length = len(s)

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(length):
        for j in range(i + n, length + 1):
            sub = s[i:j]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes