def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char <= 'W' or char >= 'y':
            filtered_chars.append(char)
    return ''.join(filtered_chars)