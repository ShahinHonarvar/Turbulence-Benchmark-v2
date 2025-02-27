def filter_chars(string):
    filtered = ''
    for char in string:
        if char < 'E' or char > 't':
            filtered += char
    return filtered