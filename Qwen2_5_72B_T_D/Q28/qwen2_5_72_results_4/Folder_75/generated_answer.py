def return_nth_smallest_ascii(s):
    subset = s[62:84]
    chars = sorted(set(subset))
    return chars[8] if len(chars) > 8 else None