def filter_chars(string):
    for char in string[10:15]:
        if char > 't' and char < 'v':
            string = string.replace(char, '')
    return string