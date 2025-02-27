from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:5]
    letters = [char.lower() for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(letters, len(letters)):
        for length in range(5, len(letters) + 1):
            for i in range(len(letters) - length + 1):
                candidate = ''.join(perm[i:i + length])
                if candidate == candidate[::-1]:
                    found_palindromes.add(candidate)
    return found_palindromes