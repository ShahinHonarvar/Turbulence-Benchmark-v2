def insert_after_character(string):
    result = ''
    for i, c in enumerate(string):
        result += c
        if c == 'A':
            result += 'H'
    return result