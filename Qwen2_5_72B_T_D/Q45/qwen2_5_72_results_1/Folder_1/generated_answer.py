from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:8]
    letters = ''.join(filter(str.isalpha, substring.lower()))
    found_palindromes = set()
    for permutation in permutations(letters, len(letters)):
        candidate = ''.join(permutation)
        if candidate == candidate[::-1] and len(candidate) >= 5:
            found_palindromes.add(candidate)
    return found_palindromes