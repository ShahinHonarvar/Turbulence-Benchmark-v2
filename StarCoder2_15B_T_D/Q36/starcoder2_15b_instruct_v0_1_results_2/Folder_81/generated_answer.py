def filter_chars(string):
    result = ''
    for char in string:
        if char < '6' or char > 'e':
            result += char
    return result