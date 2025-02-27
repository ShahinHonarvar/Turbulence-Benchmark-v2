from itertools import combinations

def all_substring_of_size_n(s):
    substrings = set()
    for indexes in combinations(range(len(s)), 92):
        substring = ''.join([s[i] for i in indexes])
        if len(set(substring)) == 92:
            substrings.add(substring)
    return list(substrings)