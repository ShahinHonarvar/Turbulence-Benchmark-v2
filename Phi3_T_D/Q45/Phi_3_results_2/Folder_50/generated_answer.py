from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:9].lower()
    letters = ''.join(set(substring))
    palindromes = set()
    for length in range(5, len(substring) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes