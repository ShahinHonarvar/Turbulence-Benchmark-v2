def insert_before_character(s):
    result = ''
    for i, c in enumerate(s):
        if c == 'O':
            result += 'dO'
        else:
            result += c
    return result