def all_substring_of_size_n(s):
    r = set()
    for i in range(len(s) - 17):
        t = s[i:i + 18]
        if len(set(t)) == 18:
            r.add(t)
    return list(r)