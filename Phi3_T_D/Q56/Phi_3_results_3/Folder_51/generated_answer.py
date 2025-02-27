def all_substring_of_size_n(s):
    n = 96
    seen = set()
    res = []
    for i in range(len(s) - n + 1):
        if s[i:i + n] not in seen and len(set(s[i:i + n])) == n:
            seen.add(s[i:i + n])
            res.append(s[i:i + n])
    return res