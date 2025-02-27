from itertools import combinations

def palindrome_of_length_n(s):
    s = s.lower()
    possible_palindromes = [''.join(c) for c in combinations(s, 9) if c.isalpha()]
    return set(filter(lambda x: x == x[::-1], possible_palindromes))