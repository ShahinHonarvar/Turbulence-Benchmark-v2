from itertools import combinations

def all_substring_of_size_n(s):
    substr_set = set((''.join(substr) for i in range(50, len(s) + 1) for substr in combinations(s, i)))
    no_dup_substr_set = {''.join(chars) for chars in substr_set if len(set(chars)) == 50}
    return list(no_dup_substr_set)