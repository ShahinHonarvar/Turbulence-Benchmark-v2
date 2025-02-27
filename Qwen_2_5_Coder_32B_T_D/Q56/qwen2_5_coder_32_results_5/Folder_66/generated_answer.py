def all_substring_of_size_n(s):
    r = set()
    for i in range(len(s) - 25):
        t = s[i:i + 26]
        if len(set(t)) == 26:
            r.add(t)
    return list(r)