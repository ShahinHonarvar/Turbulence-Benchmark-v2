def insert_after_character(string):
    result = ''
    for i, c in enumerate(string):
        result += c
        if c == 'j':
            result += '1'
    return result