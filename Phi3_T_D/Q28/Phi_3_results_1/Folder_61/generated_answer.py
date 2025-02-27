def return_nth_smallest_ascii(s):
    ascii_values = sorted([ord(c) for c in s[:10]])
    if len(ascii_values) < 10:
        return None
    return chr(ascii_values[9])