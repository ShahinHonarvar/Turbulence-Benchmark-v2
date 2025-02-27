def filter_chars(text):
    chars_to_remove = set((chr(i) for i in range(ord('/'), ord('6'))))
    filtered_text = ''.join((c for c in text if c not in chars_to_remove))
    return filtered_text