def filter_chars(string):
    filtered = ''
    for char in string:
        if char < 'O' or char > '}':
            filtered += char
    return filtered