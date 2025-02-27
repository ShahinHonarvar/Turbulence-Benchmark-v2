def filter_chars(string):
    for char in string[515:539]:
        if '+' <= char <= '}':
            string = string.replace(char, '')
    return string