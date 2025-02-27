def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'm':
            result += 'Qm'
        else:
            result += c
    return result