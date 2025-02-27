def return_nth_smallest_ascii(s):
    s_slice = s[4:34]
    ascii_chars = sorted(s_slice)
    return ascii_chars[3]