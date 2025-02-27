def filter_chars(text):
    filtered_chars = []
    for char in text:
        if char < 'X' or char > 'p':
            filtered_chars.append(char)
    return ''.join(filtered_chars)