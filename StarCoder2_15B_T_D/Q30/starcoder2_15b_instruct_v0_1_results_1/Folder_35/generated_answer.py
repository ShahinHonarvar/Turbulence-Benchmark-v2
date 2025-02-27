def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == '9':
            result += 'M9'
        else:
            result += c
    return result