from itertools import combinations

def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for length in range(53, len(s) - i + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)) and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes