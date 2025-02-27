from itertools import combinations

def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        for comb in combinations(s, 143):
            substring = ''.join(comb)
            if len(substring) == 143 and len(set(substring)) == 143:
                substrings.add(substring)
    return list(substrings)