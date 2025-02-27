from itertools import combinations

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]
    for i in range(len(s)):
        for j in range(i + 42, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes