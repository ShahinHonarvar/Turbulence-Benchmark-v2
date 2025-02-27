def filter_chars(string):
    filtered = ''
    for char in string:
        if char < 'V' or char > 'o' or (char < 'a' and char > 'Z'):
            filtered += char
    return filtered