def filter_chars(string):
    filtered = ''
    for char in string:
        if not (25 <= ord(char) <= 97 and 'm' <= char <= 'w'):
            filtered += char
    return filtered