def return_nth_smallest_ascii(s):
    if len(s) > 8:
        s = s[:9]
    chars = sorted(list(s))
    return chars[8]