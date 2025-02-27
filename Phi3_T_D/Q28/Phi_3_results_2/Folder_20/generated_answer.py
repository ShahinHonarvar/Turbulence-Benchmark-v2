def return_nth_smallest_ascii(s):
    ascii_values = sorted([ord(c) for c in s[25:65]] if len(s) > 64 else [])
    return chr(ascii_values[5]) if len(ascii_values) > 5 else None