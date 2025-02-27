def return_nth_smallest_ascii(s):
    t = sorted(s[:10])
    return t[9] if len(t) > 9 else None