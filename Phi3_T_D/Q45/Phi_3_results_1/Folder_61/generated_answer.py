from itertools import permutations
import string

def palindromes_between_indices(s):
    lower_s = s.lower()[0:8]
    letters = [char for char in lower_s if char in string.ascii_lowercase]
    unique_letters = ''.join(set(letters))
    palindromes = set()
    for perm in permutations(unique_letters * 4, 7):
        candidate = ''.join(perm).center(7)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes