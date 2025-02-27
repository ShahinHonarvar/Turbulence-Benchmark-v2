def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 37):
        t = s[i:i + 38]
        if len(set(t)) == 38:
            l.add(t)
    return list(l)