def filter_chars(string):
    filtered = ''
    for char in string:
        if (char < 'w' or char > '{') or (string.index(char) < 23 or string.index(char) > 89):
            filtered += char
    return filtered