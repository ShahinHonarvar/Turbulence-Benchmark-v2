def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('/'), ord('8') + 1) if 384 <= i - ord('a') + 1 <= 411))
    filtered_str = ''.join((c for c in s if c not in chars_to_remove))
    return filtered_str