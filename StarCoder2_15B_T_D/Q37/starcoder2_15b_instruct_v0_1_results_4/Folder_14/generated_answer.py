def filter_chars(string):
    new_string = ''
    for char in string:
        if not 35 <= ord(char) <= 98 or not 'A' <= char <= 'b':
            new_string += char
    return new_string