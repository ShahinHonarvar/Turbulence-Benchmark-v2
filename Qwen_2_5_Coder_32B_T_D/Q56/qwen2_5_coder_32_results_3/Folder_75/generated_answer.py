def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 15):
        sub = s[i:i + 16]
        if len(set(sub)) == 16:
            l.add(sub)
    return list(l)