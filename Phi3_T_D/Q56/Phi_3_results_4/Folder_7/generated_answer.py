from itertools import combinations

def all_substring_of_size_n(s):
    substrings = set()
    for idx in range(len(s) - 116):
        sub = s[idx:idx + 117]
        if len(set(sub)) == 117:
            substrings.add(sub)
    return list(substrings)