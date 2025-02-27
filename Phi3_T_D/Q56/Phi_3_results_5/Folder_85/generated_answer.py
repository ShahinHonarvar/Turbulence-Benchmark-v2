from collections import OrderedDict

def all_substring_of_size_n(s):
    distinct_substrings = OrderedDict()
    n = 14
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            distinct_substrings[substring] = True
    return list(distinct_substrings.keys())