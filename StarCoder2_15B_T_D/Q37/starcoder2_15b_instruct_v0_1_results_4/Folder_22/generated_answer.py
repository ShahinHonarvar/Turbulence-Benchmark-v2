def filter_chars(text):
    filtered_text = ''
    for char in text:
        if not (33 <= ord(char) <= 70 and char.isprintable() and ('7' <= char <= 'k')):
            filtered_text += char
    return filtered_text