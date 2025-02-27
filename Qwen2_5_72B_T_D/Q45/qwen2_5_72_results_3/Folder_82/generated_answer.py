from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:7].lower()
    letters = ''.join(filter(str.isalpha, substring))
    found_palindromes = set()
    for perm in permutations(letters, len(letters)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 7:
            found_palindromes.add(candidate)
    return found_palindromes