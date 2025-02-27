def return_nth_smallest_ascii(s):
    t = sorted(s[10:83])[:18]
    return t[17] if len(t) >= 18 else None