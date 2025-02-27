def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'N':
            result += 'z'
        result += c
    return result