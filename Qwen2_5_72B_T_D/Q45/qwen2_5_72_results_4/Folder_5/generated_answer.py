from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:9].lower()
    all_letters = ''.join(filter(str.isalpha, substring))
    found_palindromes = set()
    for perm in permutations(all_letters, len(all_letters)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            found_palindromes.add(candidate)
    return found_palindromes