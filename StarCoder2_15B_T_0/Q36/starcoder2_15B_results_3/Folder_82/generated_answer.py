def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char <= 'V' or char >= 'j':
            filtered_chars.append(char)
    return ''.join(filtered_chars)