def insert_before_character(string):
    new_string = ''
    for i, c in enumerate(string):
        if c == 'O':
            new_string += 'QO'
        else:
            new_string += c
    return new_string