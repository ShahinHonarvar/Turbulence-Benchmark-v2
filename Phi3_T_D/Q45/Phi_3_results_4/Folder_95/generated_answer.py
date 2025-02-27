from itertools import permutations

def palindromes_between_indices(s):
    if len(s) > 15 or len(s) < 7:
        return set()
    valid_chars = sorted([char for char in s[7:9] if char.isalpha()])
    combinations = set()
    for _ in range(1, min(4, len(valid_chars))):
        for perm in set(permutations(valid_chars, _)):
            combinations.add(''.join(perm).lower())
    palindromes = {comb[0] + comb[1] + comb[0] for comb in combinations}
    palindromes.update({comb[0] + comb[1] + ''.join(sorted(comb[0] + comb[1]))[::-1][0] + comb[1] + comb[0] for comb in combinations})
    return {pal for pal in palindromes if pal == pal[::-1]}