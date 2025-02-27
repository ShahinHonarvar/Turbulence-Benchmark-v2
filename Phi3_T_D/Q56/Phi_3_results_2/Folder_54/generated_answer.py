def all_substring_of_size_n(s):
    substrings = {s[i:i + 28] for i in range(len(s) - 27)}
    return [sub for sub in substrings if len(set(sub)) == 28]