def return_nth_smallest_ascii(s):
    substr = s[29:48]
    ascii_chars = [ord(c) for c in substr]
    ascii_chars.sort()
    return chr(ascii_chars[6])