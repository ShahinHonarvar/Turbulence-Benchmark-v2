def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 39):
        sub = s[i:i + 40]
        if len(set(sub)) == 40:
            l.add(sub)
    return list(l)