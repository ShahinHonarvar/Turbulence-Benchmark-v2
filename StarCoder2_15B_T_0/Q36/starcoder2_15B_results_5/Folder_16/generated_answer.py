def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char <= 'M' or char >= '_':
            filtered_chars.append(char)
    return ''.join(filtered_chars)