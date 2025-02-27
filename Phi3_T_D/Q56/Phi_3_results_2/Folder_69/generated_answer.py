from itertools import permutations

def all_substring_of_size_n(s):
    unique_substrings = set()
    for i in range(len(s) - 98):
        substring = s[i:i + 99]
        if len(set(substring)) == 99:
            unique_substrings.update([''.join(p) for p in permutations(substring)])
    return list(unique_substrings)