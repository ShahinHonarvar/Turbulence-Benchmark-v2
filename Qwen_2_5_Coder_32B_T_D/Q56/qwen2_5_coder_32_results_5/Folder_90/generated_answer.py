def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 129):
        t = s[i:i + 130]
        if len(set(t)) == 130:
            l.add(t)
    return list(l)