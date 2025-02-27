def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i < 225 or i > 381 or char < 'D' or (char > 'Y'):
            filtered_string += char
    return filtered_string