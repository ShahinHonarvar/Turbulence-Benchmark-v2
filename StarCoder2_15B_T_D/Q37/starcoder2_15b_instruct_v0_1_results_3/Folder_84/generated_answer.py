def filter_chars(text):
    chars_to_remove = set((chr(c) for c in range(ord('6'), ord('A') + 1)))
    filtered_text = ''
    for i, char in enumerate(text):
        if i < 138 or i > 920 or char not in chars_to_remove:
            filtered_text += char
    return filtered_text