from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:9].lower()
    letters = ''.join(filter(str.isalpha, substring))
    found_palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes