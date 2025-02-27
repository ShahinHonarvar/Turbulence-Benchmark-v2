from itertools import combinations

def all_substring_of_size_n(s):
    substrings = set()
    if len(s) < 79:
        return []
    for i in range(len(s) - 78):
        substring = s[i:i + 79]
        if len(set(substring)) == 79:
            substrings.add(substring)
    return list(substrings)