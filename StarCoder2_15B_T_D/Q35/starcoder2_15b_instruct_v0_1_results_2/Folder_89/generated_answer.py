def remove_repeat_chars(text):
    chars_to_remove = {}
    for i, char in enumerate(text):
        if 55 < i < 84 and text.count(char) > 1:
            chars_to_remove[char] = None
    new_text = ''
    for char in text:
        if char not in chars_to_remove:
            new_text += char
    return new_text