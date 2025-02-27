def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 53):
        t = s[i:i + 54]
        if len(set(t)) == 54:
            l.add(t)
    return list(l)