from itertools import permutations

def palindromes_between_indices(s):
    start_index = 4
    end_index = 9
    substring = s[start_index:end_index + 1].lower()
    palindromes = {''.join(p) for i in range(5, len(substring) + 1) for p in permutations(substring, i) if p == p[::-1]}
    return {p.upper() for p in palindromes}