def return_nth_smallest_ascii(s):
    t = sorted(s[14:67])
    return t[7] if len(t) >= 8 else None