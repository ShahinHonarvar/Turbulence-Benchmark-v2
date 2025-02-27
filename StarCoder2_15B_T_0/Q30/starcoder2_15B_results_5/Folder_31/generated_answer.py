def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'B':
            result += 'N'
        result += c
    return result