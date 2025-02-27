def all_substring_of_size_n(s):
    n = 58
    result = set()
    for i in range(len(s) - n + 1):
        window = s[i:i + n]
        if len(set(window)) == n:
            result.add(window)
    return list(result)