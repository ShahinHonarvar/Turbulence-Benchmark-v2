def filter_chars(s):
    exclude_range = set((chr(c) for c in range(ord('9'), ord('w') + 1)))
    return ''.join((c for i, c in enumerate(s) if i < 503 or i > 753 or c not in exclude_range))