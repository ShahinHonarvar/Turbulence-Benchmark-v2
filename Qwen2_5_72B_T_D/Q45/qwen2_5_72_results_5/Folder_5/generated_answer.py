from itertools import permutations

def palindromes_between_indices(s):
    substr = s[4:9]
    chars = [char for char in substr if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(chars):
        candidate = ''.join(perm)
        if candidate.lower() == candidate[::-1].lower() and len(candidate) >= 4:
            found_palindromes.add(candidate)
    return found_palindromes