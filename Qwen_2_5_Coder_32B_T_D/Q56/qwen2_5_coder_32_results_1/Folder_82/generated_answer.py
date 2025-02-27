def all_substring_of_size_n(s):
    l = len(s)
    r = set()
    for i in range(l - 99):
        t = s[i:i + 100]
        if len(set(t)) == 100:
            r.add(t)
    return list(r)