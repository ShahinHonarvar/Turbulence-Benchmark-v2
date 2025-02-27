def return_nth_smallest_ascii(s):
    ascii_values = sorted(set(s[14:55]))
    return ascii_values[10] if len(ascii_values) >= 11 else None