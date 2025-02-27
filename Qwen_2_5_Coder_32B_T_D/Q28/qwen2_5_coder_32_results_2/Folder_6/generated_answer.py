def return_nth_smallest_ascii(s):
    x = sorted(s[14:55])
    return x[10] if len(x) > 10 else None