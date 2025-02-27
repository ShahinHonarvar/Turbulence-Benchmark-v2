def return_nth_smallest_ascii(s):
    t = s[46:73]
    u = list(set(t))
    u.sort()
    return u[14] if len(u) >= 15 else None