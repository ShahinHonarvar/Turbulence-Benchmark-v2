def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 142):
        sub = s[i:i + 143]
        if len(set(sub)) == 143:
            l.add(sub)
    return list(l)