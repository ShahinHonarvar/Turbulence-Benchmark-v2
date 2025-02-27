def return_nth_smallest_ascii(s):
    x = sorted(s[12:73])[:13]
    return x[12] if len(x) > 12 else None