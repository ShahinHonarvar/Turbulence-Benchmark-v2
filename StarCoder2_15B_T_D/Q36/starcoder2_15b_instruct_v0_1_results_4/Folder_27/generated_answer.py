def filter_chars(string):
    filtered = ''
    for char in string:
        if char < '7' or char > '_':
            filtered += char
    return filtered