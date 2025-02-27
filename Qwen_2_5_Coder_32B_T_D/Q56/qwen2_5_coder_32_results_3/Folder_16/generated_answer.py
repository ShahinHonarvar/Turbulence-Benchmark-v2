def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 123):
        if len(set(s[i:i + 124])) == 124:
            l.add(s[i:i + 124])
    return list(l)