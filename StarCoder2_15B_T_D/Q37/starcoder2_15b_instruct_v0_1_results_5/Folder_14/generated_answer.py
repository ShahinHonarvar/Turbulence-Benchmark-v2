def filter_chars(s):
    chars_to_remove = set((chr(c) for c in range(ord('A'), ord('b') + 1) if 35 <= c <= 98))
    filtered_string = ''.join((c for c in s if c not in chars_to_remove))
    return filtered_string