def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 123):
        sub = s[i:i + 124]
        if len(set(sub)) == 124:
            l.add(sub)
    return list(l)