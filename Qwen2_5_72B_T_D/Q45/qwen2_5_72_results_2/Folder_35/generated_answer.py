from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:5]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    found_palindromes = set()
    for perm in permutations(letters, 3):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            for length in range(4, len(candidate) + 2, 2):
                expanded = candidate + candidate[:length // 2][::-1]
                found_palindromes.add(expanded)
    return found_palindromes