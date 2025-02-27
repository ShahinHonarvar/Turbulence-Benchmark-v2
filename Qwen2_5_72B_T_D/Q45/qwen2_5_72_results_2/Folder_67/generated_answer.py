from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:7].lower()
    valid_chars = ''.join(filter(lambda x: x.isalpha(), substring))
    found_palindromes = set()
    for perm in permutations(valid_chars, len(valid_chars)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 5:
            found_palindromes.add(candidate)
    return found_palindromes