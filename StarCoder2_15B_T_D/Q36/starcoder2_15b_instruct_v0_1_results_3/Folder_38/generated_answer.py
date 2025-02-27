def filter_chars(string):
    filtered = ''
    for i, c in enumerate(string):
        if i >= 44 and i < 48:
            if ord(c) > ord('+') and ord(c) < ord('l'):
                filtered += string.replace(c, '')
            else:
                filtered += c
        else:
            filtered += c
    return filtered