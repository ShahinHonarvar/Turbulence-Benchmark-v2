def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'F':
            result += 'u'
        result += c
    return result