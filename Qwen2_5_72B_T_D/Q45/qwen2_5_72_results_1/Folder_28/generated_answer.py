from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:6].lower()
    letters = ''.join(filter(str.isalpha, substring))
    found_palindromes = set()
    for permutation in permutations(letters):
        candidate = ''.join(permutation)
        if len(candidate) >= 4 and candidate == candidate[::-1]:
            found_palindromes.add(candidate)
    return found_palindromes