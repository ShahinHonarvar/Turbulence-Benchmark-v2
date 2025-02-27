def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char <= 'I' or char >= 'M':
            filtered_chars.append(char)
    return ''.join(filtered_chars)