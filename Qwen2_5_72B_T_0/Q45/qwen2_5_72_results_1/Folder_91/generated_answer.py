from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:7].lower()
    found_palindromes = set()
    for length in range(3, 6):
        for perm in permutations(substring, length):
            if perm == perm[::-1]:
                found_palindromes.add(''.join(perm))
    return found_palindromes