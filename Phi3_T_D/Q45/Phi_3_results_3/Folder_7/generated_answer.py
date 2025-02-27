from itertools import permutations

def palindromes_between_indices(s):
    sub_s = s[1:9].lower()
    sub_s_set = set(sub_s)
    palindromes = {''.join(p) for p in permutations(sub_s) if len(p) >= 7 and p == p[::-1]}
    return palindromes