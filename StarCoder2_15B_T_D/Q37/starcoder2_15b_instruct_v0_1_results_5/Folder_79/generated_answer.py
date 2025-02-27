def filter_chars(s: str) -> str:
    chars_to_remove = set((chr(c) for c in range(ord('@'), ord('U'))))
    return ''.join((c for c in s if c not in chars_to_remove or s.index(c) < 10 or s.index(c) > 52))