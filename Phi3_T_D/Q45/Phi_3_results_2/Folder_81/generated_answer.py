from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7]
    s = ''.join(filter(str.isalpha, s)).lower()
    unique_letters = sorted(set(s), key=s.index)
    palindromes = set()
    for length in range(3, len(unique_letters) + 1):
        for perm in permutations(unique_letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes