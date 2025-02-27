def insert_after_character(string):
    new_string = ''
    for i, c in enumerate(string):
        new_string += c
        if c == 'M':
            new_string += 'f'
    return new_string