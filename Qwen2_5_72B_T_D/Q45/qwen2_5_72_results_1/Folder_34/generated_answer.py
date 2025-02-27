import itertools

def palindromes_between_indices(s):
    substring = s[5:8].lower()
    unique_combinations = set([''.join(p) for p in itertools.permutations(substring)])
    palindromes = set()
    for combination in unique_combinations:
        if combination == combination[::-1] and len(combination) >= 4:
            palindromes.add(combination)
    return palindromes