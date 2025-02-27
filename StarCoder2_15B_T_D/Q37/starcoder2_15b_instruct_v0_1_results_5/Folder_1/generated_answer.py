def filter_chars(string):
    filtered = ''
    for char in string:
        if not (41 <= ord(char) <= 79 and ord('f') <= ord(char) <= ord('|')):
            filtered += char
    return filtered