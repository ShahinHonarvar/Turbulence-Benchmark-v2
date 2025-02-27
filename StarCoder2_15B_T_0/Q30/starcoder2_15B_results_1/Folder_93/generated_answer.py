def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'Y':
            result += '4'
        result += c
    return result