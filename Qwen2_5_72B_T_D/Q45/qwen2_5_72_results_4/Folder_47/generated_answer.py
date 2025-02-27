from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:8].lower()
    all_chars = ''.join(substring)
    found_palindromes = set()
    for i in range(5, len(all_chars) + 1):
        for perm in permutations(all_chars, i):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes