def all_substring_of_size_n(s):
    n = 27
    if len(s) < n:
        return []
    substrs = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == n:
            substrs.add(substr)
    return list(substrs)