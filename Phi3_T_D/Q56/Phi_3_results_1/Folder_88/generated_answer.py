def all_substring_of_size_n(s):
    n = 68
    results = set()
    seen = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(seen.intersection(substring)) == 0:
            results.add(substring)
            seen.update(substring)
    return list(results)