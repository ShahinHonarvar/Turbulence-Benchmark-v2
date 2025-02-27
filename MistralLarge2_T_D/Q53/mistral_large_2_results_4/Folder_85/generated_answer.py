import re

def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    s = re.sub('[^a-zA-Z]', '', s)
    length = len(s)
    for i in range(length):
        for j in range(i + 85, length + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes