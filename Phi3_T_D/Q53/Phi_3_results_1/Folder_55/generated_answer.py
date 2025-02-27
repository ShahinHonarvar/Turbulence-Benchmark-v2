from itertools import combinations

def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    potential_palindromes = set()
    for start, end in combinations(range(len(s)), 2):
        substring = s[start:end + 1]
        if is_palindrome(substring) and len(substring) >= 83:
            potential_palindromes.add(substring)
    return potential_palindromes