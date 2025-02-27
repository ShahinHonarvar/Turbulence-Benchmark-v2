def filter_chars(string):
    filtered = ''
    for char in string:
        if not (31 <= ord(char) <= 38 and ';' <= char <= 'g'):
            filtered += char
    return filtered