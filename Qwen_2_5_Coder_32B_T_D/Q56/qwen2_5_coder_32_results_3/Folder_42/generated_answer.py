def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 44):
        sub = s[i:i + 45]
        if len(set(sub)) == 45:
            l.add(sub)
    return list(l)