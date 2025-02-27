def return_nth_smallest_ascii(s):
    t = sorted(s[:70])[:10]
    return t[9] if len(t) == 10 else None