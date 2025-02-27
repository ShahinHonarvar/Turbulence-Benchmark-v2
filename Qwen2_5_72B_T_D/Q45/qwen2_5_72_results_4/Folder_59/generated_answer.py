from itertools import permutations

def palindromes_between_indices(s):
    chars = s[8:10].lower()
    found_palindromes = set()
    for L in range(3, len(chars) + 1):
        for subset in permutations(chars, L):
            candidate = ''.join(subset)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes