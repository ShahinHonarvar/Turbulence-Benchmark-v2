def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if i < 19 or i > 90 or (not 'F' <= char <= 'h'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)