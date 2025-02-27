from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:9].lower()
    letters = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                found_palindromes.add(''.join(perm))
    return found_palindromes