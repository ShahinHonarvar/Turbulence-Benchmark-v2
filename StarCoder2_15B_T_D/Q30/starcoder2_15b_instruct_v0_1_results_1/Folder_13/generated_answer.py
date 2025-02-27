def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'x':
            result += 'Nx'
        else:
            result += c
    return result