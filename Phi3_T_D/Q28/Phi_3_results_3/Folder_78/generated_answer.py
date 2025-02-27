def return_nth_smallest_ascii(s):
    subset = s[0:88]
    chars = sorted(set(subset), key=ord)
    return chars[13] if len(chars) >= 14 else None