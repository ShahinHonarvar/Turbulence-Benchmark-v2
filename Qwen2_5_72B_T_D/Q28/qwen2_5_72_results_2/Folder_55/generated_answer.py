def return_nth_smallest_ascii(s):
    if len(s) > 12:
        s = s[:13]
    sorted_chars = sorted(s)
    return sorted_chars[12]