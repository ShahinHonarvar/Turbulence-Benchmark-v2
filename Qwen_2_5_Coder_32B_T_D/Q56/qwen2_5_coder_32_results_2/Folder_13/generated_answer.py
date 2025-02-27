def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 52):
        if len(set(s[i:i + 53])) == 53:
            l.add(s[i:i + 53])
    return list(l)