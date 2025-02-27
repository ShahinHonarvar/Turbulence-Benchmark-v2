def filter_chars(text):
    chars_to_remove = set((chr(i) for i in range(ord('+'), ord('l'))))
    filtered_text = ''
    for char in text:
        if char not in chars_to_remove:
            filtered_text += char
    return filtered_text