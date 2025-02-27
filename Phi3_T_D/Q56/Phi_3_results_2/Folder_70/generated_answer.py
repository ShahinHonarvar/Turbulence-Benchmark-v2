def all_substring_of_size_n(s):
    n = 12
    seen = set()
    substrings = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == n and substr not in seen:
            substrings.add(substr)
            seen.add(substr)
    return list(substrings)