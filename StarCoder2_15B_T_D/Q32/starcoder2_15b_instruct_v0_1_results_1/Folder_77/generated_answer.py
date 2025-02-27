def insert_after_character(string):
    result = ''
    for i, c in enumerate(string):
        result += c
        if c == '9':
            result += 'h'
    return result