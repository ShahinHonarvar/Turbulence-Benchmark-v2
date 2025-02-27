def filter_chars(text):
    filtered_chars = []
    for char in text:
        if char <= 't' or char >= 'x':
            filtered_chars.append(char)
    return ''.join(filtered_chars)