def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if i < 421 or i >= 854:
            result += char
        elif not 'D' < char < 'J':
            result += char
    return result