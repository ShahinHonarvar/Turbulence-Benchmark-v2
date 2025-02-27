def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 97):
        if len(set(s[i:i + 98])) == 98:
            l.add(s[i:i + 98])
    return list(l)