def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 109):
        t = s[i:i + 110]
        if len(set(t)) == 110:
            l.add(t)
    return list(l)