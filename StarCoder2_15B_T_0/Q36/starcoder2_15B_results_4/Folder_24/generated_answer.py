def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char <= 't' or char >= 'v':
            filtered_chars.append(char)
    return ''.join(filtered_chars)