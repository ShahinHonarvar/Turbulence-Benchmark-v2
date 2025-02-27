def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 11):
        t = s[i:i + 12]
        if len(set(t)) == 12:
            l.add(t)
    return list(l)