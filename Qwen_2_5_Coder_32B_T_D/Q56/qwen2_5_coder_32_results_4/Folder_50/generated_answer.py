def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 10):
        substring = s[i:i + 11]
        if len(set(substring)) == 11:
            l.add(substring)
    return list(l)