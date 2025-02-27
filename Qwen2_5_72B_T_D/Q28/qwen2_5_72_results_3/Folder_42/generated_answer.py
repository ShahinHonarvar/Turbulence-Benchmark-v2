def return_nth_smallest_ascii(s):
    chars = sorted([s[i] for i in range(12, min(73, len(s)))])
    return chars[12] if len(chars) > 12 else None