def all_substring_of_size_n(s):
    r = set()
    for i in range(len(s) - 46):
        t = s[i:i + 47]
        if len(set(t)) == 47:
            r.add(t)
    return list(r)