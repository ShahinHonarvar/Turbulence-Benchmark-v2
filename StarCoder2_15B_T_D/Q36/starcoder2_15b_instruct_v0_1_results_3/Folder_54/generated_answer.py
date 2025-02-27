def filter_chars(text):
    filtered = ''
    for char in text:
        if char <= ')' or char >= 'P':
            filtered += char
    return filtered