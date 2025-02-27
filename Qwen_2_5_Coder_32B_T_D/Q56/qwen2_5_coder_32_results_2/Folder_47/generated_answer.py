def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 90):
        if len(set(s[i:i + 91])) == 91:
            l.add(s[i:i + 91])
    return list(l)