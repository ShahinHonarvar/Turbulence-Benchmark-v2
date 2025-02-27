def all_substring_of_size_n(s):
    substrings = set()
    length = 38
    n = len(s)
    for i in range(n - length + 1):
        substr = s[i:i + length]
        if len(set(substr)) == length:
            substrings.add(substr)
    return list(substrings)