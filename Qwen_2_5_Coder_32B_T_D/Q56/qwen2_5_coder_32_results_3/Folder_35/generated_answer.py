def all_substring_of_size_n(s):
    r = set()
    for i in range(len(s) - 26):
        t = s[i:i + 27]
        if len(set(t)) == 27:
            r.add(t)
    return list(r)