def all_substring_of_size_n(s):
    res = set()
    for i in range(len(s) - 85):
        sub = s[i:i + 86]
        if len(set(sub)) == 86:
            res.add(sub)
    return list(res)