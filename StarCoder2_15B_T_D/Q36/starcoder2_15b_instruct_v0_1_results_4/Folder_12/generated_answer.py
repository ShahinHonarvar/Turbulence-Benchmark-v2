def filter_chars(text):
    filtered_text = ''
    for char in text:
        if char < 'm' or char > 'w':
            filtered_text += char
    return filtered_text