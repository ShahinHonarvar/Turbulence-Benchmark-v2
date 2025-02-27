def insert_after_character(string):
    new_string = ''
    for i, c in enumerate(string):
        new_string += c
        if c == 'w':
            new_string += 'n'
    return new_string