from itertools import permutations

def palindromes_between_indices(s):
    substr = s[4:8].lower()
    letters = ''.join(filter(str.isalpha, substr))
    found_palindromes = set()
    for perm in permutations(letters):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            found_palindromes.add(candidate)
    return found_palindromes