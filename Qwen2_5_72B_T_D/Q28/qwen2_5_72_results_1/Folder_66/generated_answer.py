def return_nth_smallest_ascii(s):
    s = s[35:53]
    s = sorted(set(s))
    return s[9] if len(s) > 9 else None