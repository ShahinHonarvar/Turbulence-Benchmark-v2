def all_substring_of_size_n(s):
    n = 124
    distinct_substrings = set()
    for start in range(len(s) - n + 1):
        if len(set(s[start:start + n])) == n:
            distinct_substrings.add(s[start:start + n])
    return list(distinct_substrings)