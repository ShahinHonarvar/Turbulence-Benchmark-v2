from itertools import permutations, combinations_with_replacement

def palindromes_between_indices(s):
    s = s[1:8].lower()
    letters = set(s)
    palindromes = set()
    for length in range(6, len(s) + 1):
        for combo in combinations_with_replacement(letters, length):
            for perm in permutations(combo):
                if perm == perm[::-1]:
                    palindromes.add(''.join(perm))
    return palindromes