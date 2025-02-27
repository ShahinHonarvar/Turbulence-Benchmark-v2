def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'U':
            result += 'T'
        result += c
    return result