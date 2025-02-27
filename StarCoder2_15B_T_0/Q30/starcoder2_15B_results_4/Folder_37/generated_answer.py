def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'U':
            result += 'aU'
        else:
            result += c
    return result