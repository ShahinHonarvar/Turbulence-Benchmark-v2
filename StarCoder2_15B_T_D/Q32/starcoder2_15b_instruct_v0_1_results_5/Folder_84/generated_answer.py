def insert_after_character(string):
    result = ''
    for i, c in enumerate(string):
        result += c
        if c == 'H':
            result += 'n'
    return result