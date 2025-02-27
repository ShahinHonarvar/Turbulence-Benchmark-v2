from itertools import product

def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    min_length, max_length = (30, 46)
    desired_substring = s[26:85]
    candidates = set((''.join(candidate) for candidate in product(*[(c.upper() + c.lower(),) * 2 for c in desired_substring]) if min_length <= len(candidate) <= max_length))
    return {palindrome for palindrome in candidates if is_palindrome(palindrome)}