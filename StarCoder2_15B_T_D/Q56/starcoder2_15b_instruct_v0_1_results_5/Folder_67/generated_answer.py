def all_substring_of_size_n(s):
    res = set()
    n = 43
    for i in range(len(s) - n + 1):
        if len(set(s[i:i + n])) == n:
            res.add(s[i:i + n])
    return list(res)