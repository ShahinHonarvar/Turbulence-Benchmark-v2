from itertools import permutations

def palindromes_between_indices(text):
    substring = text[3:8].lower()
    unique_chars = set(substring)
    all_perms = set(permutations(unique_chars, 4))
    palindromes = {''}
    for perm in all_perms:
        if perm[0] == perm[-1]:
            middle = ''.join(perm[1:-1])
            palindromes.add(perm[0] + middle + perm[0])
    return palindromes