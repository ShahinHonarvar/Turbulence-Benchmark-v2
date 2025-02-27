def filter_chars(string):
    new_string = ''
    for i, char in enumerate(string):
        if i < 54 or i >= 92:
            new_string += char
        elif char <= 'J' or char >= 'X':
            new_string += char
    return new_string