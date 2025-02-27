def return_nth_smallest_ascii(s):
    target_chars = s[51:79]
    ascii_values = sorted((ord(c) for c in target_chars))
    return chr(ascii_values[8])