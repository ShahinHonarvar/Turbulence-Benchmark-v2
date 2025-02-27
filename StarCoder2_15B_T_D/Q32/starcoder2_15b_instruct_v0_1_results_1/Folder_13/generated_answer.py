def insert_after_character(string):
    new_string = ''
    for i, c in enumerate(string):
        if c == 'x':
            new_string += 'Nx'
        else:
            new_string += c
    return new_string