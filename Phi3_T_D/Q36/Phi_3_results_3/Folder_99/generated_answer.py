def filter_chars(s):
    start, end = (476, 948)
    char_range_mask = ''.join((chr(i) for i in range(ord('b'), ord('d'))))
    filtered_chars = ''.join((c for c in s[start:end] if c not in char_range_mask))
    return s[:start] + filtered_chars + s[end:]