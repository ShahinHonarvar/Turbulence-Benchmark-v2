from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:10].lower()
    palindromes = set((''.join(p) for p in set(permutations(substring)) if p == p[::-1]))
    palindromes_len_4_or_more = {p for p in palindromes if len(p) >= 4}
    return palindromes_len_4_or_more