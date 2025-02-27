def filter_chars(s):
    s, filtered_chars = (list(s), [])
    for i in range(13, 29):
        c, n = ('c', 'n')
        filtered_chars += [s[i]] if not c <= s[i] <= n else []
    for char in filtered_chars:
        del s[13:29 + 1][s[13:29 + 1].index(char)]
    return ''.join(s)