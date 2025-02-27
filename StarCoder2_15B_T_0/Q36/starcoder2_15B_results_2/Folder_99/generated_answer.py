def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char <= 'b' or char >= 'd':
            filtered_chars.append(char)
    return ''.join(filtered_chars)