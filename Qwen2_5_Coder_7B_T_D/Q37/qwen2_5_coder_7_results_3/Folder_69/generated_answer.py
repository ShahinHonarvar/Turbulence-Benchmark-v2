def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('!'), ord('x') + 1)))
    result = [c for i, c in enumerate(s) if i < 114 or i > 639 or c not in chars_to_remove]
    return ''.join(result)