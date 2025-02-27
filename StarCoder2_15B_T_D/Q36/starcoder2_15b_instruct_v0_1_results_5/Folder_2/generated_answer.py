def filter_chars(string):
    new_chars = []
    for char in string:
        if char <= 'D' or char >= 'J':
            new_chars.append(char)
    return ''.join(new_chars)