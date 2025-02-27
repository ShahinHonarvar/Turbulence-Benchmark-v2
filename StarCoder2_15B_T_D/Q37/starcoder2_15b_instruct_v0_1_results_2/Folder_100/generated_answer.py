def filter_chars(string):
    filtered = ''
    for char in string:
        if char < 'J' or char > 'Q':
            filtered += char
    return filtered