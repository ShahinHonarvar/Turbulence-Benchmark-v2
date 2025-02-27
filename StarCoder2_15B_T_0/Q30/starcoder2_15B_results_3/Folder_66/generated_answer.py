def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'k':
            result += 'k'
        result += c
    return result