from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:6].lower()
    letters = ''.join(sorted(set(substring), key=substring.index))
    found_palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes