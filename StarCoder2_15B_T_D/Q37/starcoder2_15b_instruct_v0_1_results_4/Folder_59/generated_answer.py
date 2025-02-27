def filter_chars(string):
    filtered = ''
    for char in string:
        if not (char >= '5' and char <= '_' and (string.index(char) in range(2, 4))):
            filtered += char
    return filtered