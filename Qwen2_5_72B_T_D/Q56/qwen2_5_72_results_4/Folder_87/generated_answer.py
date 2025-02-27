def all_substring_of_size_n(s):
    n = 58
    substrings = [s[i:i + n] for i in range(len(s) - n + 1)]
    unique_substrings = list(set(filter(lambda x: len(x) == len(set(x)), substrings)))
    return unique_substrings