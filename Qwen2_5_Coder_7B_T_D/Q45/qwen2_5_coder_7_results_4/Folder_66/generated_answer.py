import itertools

def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = set(s)
    palindromes = set()
    for length in range(5, 7):
        for comb in itertools.combinations_with_replacement(letters, length):
            perm = set(itertools.permutations(comb))
            for p in perm:
                p_str = ''.join(p)
                if p_str == p_str[::-1]:
                    palindromes.add(p_str)
    return palindromes