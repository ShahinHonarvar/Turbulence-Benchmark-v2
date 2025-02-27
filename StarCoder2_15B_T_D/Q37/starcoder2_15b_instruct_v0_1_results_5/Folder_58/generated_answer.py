def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('9'), ord('w') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove or s.index(c) < 503 or s.index(c) > 753))