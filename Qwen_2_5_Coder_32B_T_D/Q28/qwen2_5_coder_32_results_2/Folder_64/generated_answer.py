def return_nth_smallest_ascii(s):
    t = sorted(s[:7])
    return t[6] if len(t) > 6 else None