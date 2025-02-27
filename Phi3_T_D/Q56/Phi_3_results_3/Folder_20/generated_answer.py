def all_substring_of_size_n(s):
    n = 50
    seen = set()
    substrings = [s[i:i + n] for i in range(len(s) - n + 1)]
    unique_chars_substrings = [substr for substr in substrings if len(set(substr)) == n]
    return list(unique_chars_substrings)