def all_substring_of_size_n(s):
    result = set()
    n = len(s)
    if n < 45:
        return []
    for i in range(n - 44):
        if len(set(s[i:i + 45])) == 45:
            result.add(s[i:i + 45])
    return list(result)