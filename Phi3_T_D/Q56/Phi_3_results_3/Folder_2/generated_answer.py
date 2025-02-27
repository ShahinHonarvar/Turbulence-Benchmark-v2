from itertools import permutations

def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 55):
        substring = ''.join(sorted(s[i:i + 56]))
        if len(substring) == 56 and len(set(substring)) == 56:
            substrings.add(substring)
    return list(permutations(substrings, 1))[0] if substrings else []