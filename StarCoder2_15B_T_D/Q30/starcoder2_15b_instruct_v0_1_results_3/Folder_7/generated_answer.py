def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == '':
            result += 'H'
        result += c
    return result