def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('D'), ord('Y') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove if 225 <= s.index(c) <= 381))