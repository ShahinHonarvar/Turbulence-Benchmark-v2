from itertools import permutations

def palindromes_between_indices(s):
    lower_s = s[2:7].lower()
    letters = set(lower_s)
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes