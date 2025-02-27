def filter_chars(text):
    filtered = ''
    for char in text:
        if char > 'E' and char < '~':
            continue
        filtered += char
    return filtered