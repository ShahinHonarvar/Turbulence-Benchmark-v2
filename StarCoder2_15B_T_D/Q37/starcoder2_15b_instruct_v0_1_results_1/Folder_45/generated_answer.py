def filter_chars(text):
    chars_to_remove = set()
    for i, char in enumerate(text):
        if 72 <= i <= 94 and '.' <= char <= 'b':
            chars_to_remove.add(char)
    filtered_text = ''
    for char in text:
        if char not in chars_to_remove:
            filtered_text += char
    return filtered_text