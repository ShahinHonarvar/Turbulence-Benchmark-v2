from itertools import combinations

def all_substring_of_size_n(s):
    substrings = set((s[i:i + 85] for i in range(len(s) - 84)))
    distinct_substrings = [string for string in substrings if len(set(string)) == 85]
    return distinct_substrings