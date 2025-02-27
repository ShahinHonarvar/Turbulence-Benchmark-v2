def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 31):
        t = s[i:i + 32]
        if len(set(t)) == 32:
            l.add(t)
    return list(l)