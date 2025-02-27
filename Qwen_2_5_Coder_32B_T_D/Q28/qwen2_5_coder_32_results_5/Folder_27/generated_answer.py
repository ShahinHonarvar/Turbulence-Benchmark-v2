def return_nth_smallest_ascii(s):
    a = sorted(s[33:86])[:13]
    return a[-1] if len(a) > 12 else ''