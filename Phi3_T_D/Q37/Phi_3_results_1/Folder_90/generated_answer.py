def filter_chars(string):
    for char in string[348:853]:
        if 'J' <= char <= 'b':
            string = string.replace(char, '')
    return string