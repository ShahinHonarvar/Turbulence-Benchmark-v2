def return_nth_smallest_ascii(s):
    chars = sorted(set(s[25:89]))
    return chars[10] if len(chars) > 10 else None