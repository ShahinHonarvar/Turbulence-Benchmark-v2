def all_substring_of_size_n(s):
    l = set()
    for i in range(len(s) - 5):
        substring = s[i:i + 6]
        if len(set(substring)) == 6:
            l.add(substring)
    return list(l)