def filter_chars(string):
    filtered = ''
    for char in string:
        if not (69 <= ord(char) <= 80 and '@' <= char <= 'p'):
            filtered += char
    return filtered