def return_nth_smallest_ascii(s):
    ascii_chars = sorted(s[37:60])
    if len(ascii_chars) < 6:
        return None
    return ascii_chars[5]