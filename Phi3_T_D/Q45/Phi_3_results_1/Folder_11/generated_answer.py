from itertools import permutations

def is_palindrome(s):
    s = ''.join([c.upper() for c in s if c.isalpha()])
    return s == s[::-1]

def palindromes_between_indices(s):
    sub_string = s[3:8]
    unique_chars = ''.join(set(sub_string.lower()))
    palindromes = set()
    for length in range(4, len(unique_chars) + 1):
        for perm in permutations(unique_chars, length):
            palindrome = ''.join(perm)
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes