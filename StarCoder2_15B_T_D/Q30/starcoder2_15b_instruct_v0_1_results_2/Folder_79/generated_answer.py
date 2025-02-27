def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'E':
            result += 'E'
        result += c
    return result