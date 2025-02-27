def filter_chars(text):
    new_text = ''
    for i, c in enumerate(text):
        if not (225 <= i <= 381 and 'D' <= c <= 'Y'):
            new_text += c
    return new_text