def insert_after_character(string):
    result = ''
    for i, c in enumerate(string):
        result += c
        if c == ' ':
            result += 'H'
    return result