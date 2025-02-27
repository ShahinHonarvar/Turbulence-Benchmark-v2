def filter_chars(text):
    filtered = ''
    for char in text:
        if char < 'W' or char > '{':
            filtered += char
    return filtered