def all_substring_of_size_n(s):
    n = 36
    substr_set = set()
    if len(s) < n:
        return list(substr_set)
    for i in range(len(s) - n + 1):
        substr = ''.join(sorted(s[i:i + n]))
        if len(set(substr)) == n:
            substr_set.add(substr)
    return list(substr_set)