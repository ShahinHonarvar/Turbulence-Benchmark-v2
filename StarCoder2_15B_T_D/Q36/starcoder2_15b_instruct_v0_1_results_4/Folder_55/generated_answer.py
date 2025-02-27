def filter_chars(text):
    filtered = ''
    for char in text:
        if not (char > 'Y' and char < 's'):
            filtered += char
    return filtered