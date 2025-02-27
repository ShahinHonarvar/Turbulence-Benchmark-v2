def all_substring_of_size_n(s):
    if len(s) < 58:
        return []
    substrings = {s[i:i + 58] for i in range(len(s) - 57)}
    return list(substrings)