import itertools

def palindromes_between_indices(s):
    s = s.lower()
    letters = s[1:9]
    letters_set = set(letters)
    if len(letters_set) < 7:
        return set()
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                perm_str = ''.join(perm)
                if perm_str == perm_str[::-1]:
                    palindromes.add(perm_str)
    return palindromes