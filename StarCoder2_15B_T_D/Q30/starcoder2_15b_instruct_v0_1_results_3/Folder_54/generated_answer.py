def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'M':
            result += 'f'
        result += c
    return result