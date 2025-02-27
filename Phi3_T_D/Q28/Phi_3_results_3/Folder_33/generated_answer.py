def return_nth_smallest_ascii(s):
    char_range = sorted(s[22:75])
    return char_range[11] if len(char_range) >= 12 else None