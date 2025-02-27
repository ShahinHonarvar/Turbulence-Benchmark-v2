def filter_chars(string):
    result = []
    for char in string:
        if char <= 'B' or char >= 'z':
            result.append(char)
    return ''.join(result)