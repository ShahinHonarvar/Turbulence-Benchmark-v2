from itertools import permutations

def all_substring_of_size_n(s):
    if len(s) < 26 or len(s) != len(set(s)):
        return []
    perms = {''.join(p) for p in permutations(s)}
    return list(perms)