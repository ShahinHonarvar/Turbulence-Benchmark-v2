def return_nth_smallest_ascii(s):
    t = s[8:66]
    u = sorted(set(t))
    return u[5] if len(u) >= 6 else None