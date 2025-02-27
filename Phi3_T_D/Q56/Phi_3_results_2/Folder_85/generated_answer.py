from itertools import permutations

def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 13):
        substring = s[i:i + 14]
        if len(set(substring)) == 14:
            substrings.update([''.join(p) for p in permutations(substring)])
    return list(substrings)