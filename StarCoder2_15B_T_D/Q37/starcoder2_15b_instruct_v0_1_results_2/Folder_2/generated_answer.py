def filter_chars(text):
    filtered_text = ''
    for char in text:
        if char < ',' or char > 'V':
            filtered_text += char
    return filtered_text