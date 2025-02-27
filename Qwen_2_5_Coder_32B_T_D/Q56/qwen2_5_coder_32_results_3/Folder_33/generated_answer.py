def all_substring_of_size_n(s):
    n = 105
    result = set()
    if len(s) < n:
        return []
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == n:
            result.add(substr)
    return list(result)