def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'e':
            result += '0'
        result += c
    return result