def filter_chars(s):
    removed_chars = set()
    for i in range(71, 95):
        c = s[i]
        if 'K' <= c <= 'a':
            removed_chars.add(c)
    for char in removed_chars:
        s = s.replace(char, '')
    return s