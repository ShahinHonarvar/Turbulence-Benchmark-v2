def filter_chars(text):
    filtered_text = ''
    for char in text:
        if char < '?' or char > 'f':
            filtered_text += char
    return filtered_text