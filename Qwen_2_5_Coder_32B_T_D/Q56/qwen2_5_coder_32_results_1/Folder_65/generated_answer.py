def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 80):
        t = s[i:i + 81]
        if len(set(t)) == 81:
            l.add(t)
    return list(l)