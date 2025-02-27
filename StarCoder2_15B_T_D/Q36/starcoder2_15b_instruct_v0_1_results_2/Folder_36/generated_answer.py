def filter_chars(text):
    filtered_text = ''
    for i, c in enumerate(text):
        if i < 283 or i >= 484:
            filtered_text += c
        elif not (c > 'l' and c < 't'):
            filtered_text += c
    return filtered_text