def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('?'), ord('k') + 1)))
    filtered_chars = [c for c in s if c not in chars_to_remove or s.index(c) < 3 or s.index(c) >= 8]
    return ''.join(filtered_chars)