def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 145):
        t = s[i:i + 146]
        if len(set(t)) == 146:
            l.add(t)
    return list(l)