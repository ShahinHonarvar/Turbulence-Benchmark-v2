def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if i < 51 or i >= 76 or (not '6' <= char < 'f'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)