def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 141):
        t = s[i:i + 142]
        if len(set(t)) == 142:
            l.add(t)
    return list(l)