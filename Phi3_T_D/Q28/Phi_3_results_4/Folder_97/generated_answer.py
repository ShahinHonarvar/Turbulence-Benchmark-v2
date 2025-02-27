def return_nth_smallest_ascii(s):
    specific_chars = sorted(s[15:22])
    return specific_chars[5] if len(specific_chars) >= 6 else 'Index out of range'