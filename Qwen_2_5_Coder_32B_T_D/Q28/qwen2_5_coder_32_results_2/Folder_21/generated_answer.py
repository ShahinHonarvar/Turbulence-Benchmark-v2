def return_nth_smallest_ascii(s):
    x = sorted(s[8:66])
    return x[5] if len(x) >= 6 else None