def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 143):
        t = s[i:i + 144]
        if len(set(t)) == 144:
            l.add(t)
    return list(l)