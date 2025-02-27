def filter_chars(string):
    filtered = ''
    for char in string:
        if char > 'S' and char < 'm':
            continue
        filtered += char
    return filtered