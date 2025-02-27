def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 70):
        t = s[i:i + 71]
        if len(set(t)) == 71:
            l.add(t)
    return list(l)