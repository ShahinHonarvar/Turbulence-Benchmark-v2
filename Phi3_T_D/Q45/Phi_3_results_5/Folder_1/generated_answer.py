from itertools import permutations

def palindromes_between_indices(s):
    length = 5
    char_pool = set(s[4:8].lower())
    palindromes = set()
    if len(char_pool) >= length:
        for perm in permutations(char_pool, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes