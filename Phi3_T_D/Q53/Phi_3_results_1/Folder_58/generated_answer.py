from itertools import combinations

def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 146):
        for j in range(i + 147, len(s) + 1):
            substring = s[i:j]
            if all((c.isalpha() for c in substring)):
                if is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes