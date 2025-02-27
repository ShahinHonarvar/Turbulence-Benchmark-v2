def return_nth_smallest_ascii(s):
    subset = s[min(len(s), 74) - 22:min(len(s), 75)]
    ascii_vals = sorted([ord(ch) for ch in subset])
    if len(ascii_vals) < 12:
        return None
    return chr(ascii_vals[11])