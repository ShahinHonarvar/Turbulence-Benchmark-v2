from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:10].lower()
    letters = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(letters):
        for length in range(5, len(letters) + 1):
            candidate = ''.join(perm[:length])
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes