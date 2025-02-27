def filter_chars(s):
    chars_to_remove = set((chr(c) for c in range(ord('K'), ord('z') + 1)))
    return ''.join((c for c in s if not (29 <= s.index(c) <= 79 and c in chars_to_remove)))