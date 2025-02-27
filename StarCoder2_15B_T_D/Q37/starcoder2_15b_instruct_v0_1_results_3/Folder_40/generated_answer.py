def filter_chars(string):
    for char in string:
        if char.isprintable() and '*' <= char <= 's':
            string = string.replace(char, '')
    return string