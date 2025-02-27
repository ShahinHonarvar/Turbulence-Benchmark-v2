def all_substring_of_size_n(s):
    results = set()
    n = 3
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == n:
            results.add(substr)
    return list(results)