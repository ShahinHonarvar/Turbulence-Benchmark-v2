def filter_chars(string):
    result = []
    for char in string:
        if char < 'D' or char > 'G':
            result.append(char)
    return ''.join(result)