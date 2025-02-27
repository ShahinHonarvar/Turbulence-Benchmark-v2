from itertools import combinations

def is_valid_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    letter_positions = [i for i, c in enumerate(s) if c.isalpha()]
    for length in range(6, len(letter_positions) + 1):
        for indices in combinations(letter_positions, length):
            substr = ''.join((s[i] for i in indices))
            if is_valid_palindrome(substr):
                palindromes.add(substr)
    return palindromes