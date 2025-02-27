def all_substring_of_size_n(s):
    n = 95
    seen = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == n:
            seen.add(substr)
    return list(seen)