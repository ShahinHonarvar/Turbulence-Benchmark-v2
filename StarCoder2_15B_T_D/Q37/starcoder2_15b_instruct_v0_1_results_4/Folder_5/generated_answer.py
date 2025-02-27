def filter_chars(string):
    filtered = ''
    for char in string:
        if char >= '5' and char <= '<':
            continue
        filtered += char
    return filtered