def all_substring_of_size_n(s):
    n = len(s)
    substrings = set()
    if n < 89:
        return list(substrings)
    for i in range(n - 88):
        if len(set(s[i:i + 89])) == 89:
            substrings.add(s[i:i + 89])
    return list(substrings)