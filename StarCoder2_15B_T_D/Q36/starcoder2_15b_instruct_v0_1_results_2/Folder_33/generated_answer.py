def filter_chars(s):
    result = ''
    for index, char in enumerate(s):
        if index < 299 or index >= 418:
            result += char
        elif char > '9' and char < 'P':
            result += char
    return result