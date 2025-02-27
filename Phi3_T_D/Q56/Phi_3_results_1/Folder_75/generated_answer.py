def all_substring_of_size_n(s):
    n = 16
    substrings = set()
    unique_chars = set(s)
    if len(unique_chars) < n:
        return list(substrings)
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == n:
            substrings.add(substr)
    return list(substrings)