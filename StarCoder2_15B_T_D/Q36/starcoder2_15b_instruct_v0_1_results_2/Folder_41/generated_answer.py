def filter_chars(s):
    char_range = range(ord('f') + 1, ord('}'))
    filtered_chars = [c for c in s if c not in char_range or s.index(c) < 81 or s.index(c) >= 89]
    return ''.join(filtered_chars)