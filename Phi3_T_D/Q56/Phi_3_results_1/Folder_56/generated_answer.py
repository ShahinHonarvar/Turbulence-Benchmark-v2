from itertools import combinations

def all_substring_of_size_n(s):
    substrings = {s[i:i + 69] for i in range(len(s) - 68)}
    result = []
    for substring in substrings:
        if len(substring) == 69 and len(substring) == len(set(substring)):
            result.append(substring)
    return result