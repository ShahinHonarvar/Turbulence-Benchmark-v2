def insert_after_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'S':
            result += 'SU'
        else:
            result += c
    return result