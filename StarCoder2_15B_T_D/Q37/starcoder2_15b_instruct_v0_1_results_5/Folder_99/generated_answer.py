def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if (i < 373 or i > 901) or (char < 'T' or char > 'h'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)