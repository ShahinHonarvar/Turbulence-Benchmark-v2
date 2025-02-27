def filter_chars(s):
    lookup_table = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(43, 68):
        if lookup_table[i + 1] > 'B' and lookup_table[i + 1] < 'r':
            s = s.replace(s[i], '')
    return s