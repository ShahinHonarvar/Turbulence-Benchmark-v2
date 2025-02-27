def filter_chars(string):
    filtered = ''
    for char in string:
        if char < 'H' or char > 'e':
            filtered += char
    return filtered