def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 42):
        t = s[i:i + 43]
        if len(set(t)) == 43:
            l.add(t)
    return list(l)