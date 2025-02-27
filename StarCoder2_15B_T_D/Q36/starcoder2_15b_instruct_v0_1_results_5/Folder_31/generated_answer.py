def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i >= 14 and i < 75 and (char > '9') and (char < 'K'):
            continue
        filtered_text += char
    return filtered_text