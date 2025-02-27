def filter_chars(string):
    result = ''
    for index, char in enumerate(string):
        if index > 43 and index < 68:
            if char > 'W' and char < 'x':
                continue
        result += char
    return result