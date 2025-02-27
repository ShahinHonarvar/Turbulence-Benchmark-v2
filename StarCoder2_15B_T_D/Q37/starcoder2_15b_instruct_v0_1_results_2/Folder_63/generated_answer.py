def filter_chars(string):
    filtered = ''
    for char in string:
        if not (42 <= ord(char) <= 92 and '/' <= char <= 'a'):
            filtered += char
    return filtered