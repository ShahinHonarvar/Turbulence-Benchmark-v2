def filter_chars(s):
    for ch in [c for c in s[61:88] if '%' < c < 'q']:
        s = s.replace(ch, '')
    return s