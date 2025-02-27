from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:8]
    letters = [char.lower() for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(letters, len(letters)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            for length in range(4, len(candidate) + 1):
                if candidate[:length] == candidate[:length][::-1]:
                    found_palindromes.add(candidate[:length])
    return found_palindromes