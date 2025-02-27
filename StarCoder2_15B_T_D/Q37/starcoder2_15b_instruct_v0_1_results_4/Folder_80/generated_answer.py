def filter_chars(text):
    filtered = ''
    for char in text:
        if char < 'a' or char > 'i':
            filtered += char
    return filtered