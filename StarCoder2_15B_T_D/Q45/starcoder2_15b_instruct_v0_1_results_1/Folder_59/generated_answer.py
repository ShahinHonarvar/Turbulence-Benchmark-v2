import string
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[8:10]
    lowercase_substring = substring.lower()
    english_letters = set(string.ascii_lowercase)
    permutations_of_letters = set(permutations(lowercase_substring, len(lowercase_substring)))
    palindromes = set((p for p in permutations_of_letters if len(p) >= 3 and p == p[::-1]))
    return palindromes