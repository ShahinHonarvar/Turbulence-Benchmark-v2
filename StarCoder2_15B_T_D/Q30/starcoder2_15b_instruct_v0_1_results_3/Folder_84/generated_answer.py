def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'H':
            result += 'n'
        result += c
    return result