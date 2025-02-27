def return_nth_smallest_ascii(s):
    ascii_chars = sorted(s[0:19])
    return ascii_chars[18] if len(ascii_chars) > 18 else None