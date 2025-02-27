def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 104):
        sub = s[i:i + 105]
        if len(set(sub)) == 105:
            l.add(sub)
    return list(l)