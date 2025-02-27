def filter_chars(s):
    for ch in s[33:36]:
        if '>' < ch < 'A':
            s = s.replace(ch, '')
    return s