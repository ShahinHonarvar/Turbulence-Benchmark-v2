def filter_chars(string):
    filtered = ''
    for char in string:
        if char <= ')' or char >= 'P':
            filtered += char
    return filtered