from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:8]
    letters = ''.join([char.lower() for char in substring if char.isalpha()])
    found_palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                found_palindromes.add(''.join(perm))
    return found_palindromes