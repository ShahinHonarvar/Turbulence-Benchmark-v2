def insert_after_character(string):
    result = ''
    for i, c in enumerate(string):
        result += c
        if c == 'g':
            result += 'M'
    return result