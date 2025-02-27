def return_nth_smallest_ascii(s):
    subset = s[8:66]
    ascii_values = sorted(set((ord(c) for c in subset)))
    return chr(ascii_values[5]) if len(ascii_values) >= 6 else None