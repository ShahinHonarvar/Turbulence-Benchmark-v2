def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'P':
            result += 'V'
        result += c
    return result