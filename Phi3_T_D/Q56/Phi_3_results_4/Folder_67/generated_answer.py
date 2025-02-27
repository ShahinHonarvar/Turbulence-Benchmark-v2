def all_substring_of_size_n(s):
    size = 43
    n = len(s)
    if size > n:
        return []
    substrings = set()
    for i in range(n - size + 1):
        substr = s[i:i + size]
        if len(set(substr)) == size:
            substrings.add(substr)
    return list(substrings)