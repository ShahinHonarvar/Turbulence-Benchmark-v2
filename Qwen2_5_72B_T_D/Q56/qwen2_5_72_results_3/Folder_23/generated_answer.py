def all_substring_of_size_n(s):
    n = 42
    substr_set = set()
    for i in range(0, len(s) - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == n:
            substr_set.add(substr)
    return list(substr_set)