def filter_chars(text):
    chars_to_remove = set((chr(i) for i in range(ord('F'), ord('~'))))
    result = [c for c in text if c not in chars_to_remove]
    return ''.join(result)