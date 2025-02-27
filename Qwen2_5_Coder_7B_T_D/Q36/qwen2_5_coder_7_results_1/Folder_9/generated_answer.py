def filter_chars(s):
    for i in range(50, 92):
        ch = chr(i)
        if 'A' < ch < 'Q':
            s = s.replace(ch, '')
    return s