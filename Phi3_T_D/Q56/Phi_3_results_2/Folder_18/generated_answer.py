def all_substring_of_size_n(s):
    n = 63
    returned_substrings = {s[i:i + n] for i in range(len(s) - n + 1) if len(set(s[i:i + n])) == n}
    return list(returned_substrings)