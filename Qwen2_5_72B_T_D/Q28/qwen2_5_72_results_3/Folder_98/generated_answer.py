def return_nth_smallest_ascii(s):
    if len(s) > 8:
        s = s[:9]
    return sorted(list(s))[8]