def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord(';'), ord('g') + 1)))
    filtered = [c for c in s if c not in chars_to_remove]
    return ''.join(filtered)