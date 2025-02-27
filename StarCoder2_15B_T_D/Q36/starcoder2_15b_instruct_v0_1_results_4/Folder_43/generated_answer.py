def filter_chars(text):
    new_text = ''
    for char in text:
        if char <= 'A' or char >= 'i':
            new_text += char
    return new_text