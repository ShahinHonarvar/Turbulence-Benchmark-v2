def filter_chars(text):
    filtered_text = ''
    for i, c in enumerate(text):
        if i >= 43 and i < 69:
            if c > 'B' and c < 'r':
                continue
        filtered_text += c
    return filtered_text