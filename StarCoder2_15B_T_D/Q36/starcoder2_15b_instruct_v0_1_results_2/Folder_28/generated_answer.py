def filter_chars(string):
    result = ''
    for char in string:
        if (char < 'M' or char > 'j') or (char < 'a' or char > 'z'):
            result += char
    return result