def all_substring_of_size_n(s):
    res = set()
    for i in range(len(s) - 98):
        sub = s[i:i + 99]
        if len(set(sub)) == 99:
            res.add(sub)
    return list(res)