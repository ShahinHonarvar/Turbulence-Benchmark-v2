def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i < 221 or i >= 419:
            filtered_text += char
        elif not '-' < char < 'v':
            filtered_text += char
    return filtered_text