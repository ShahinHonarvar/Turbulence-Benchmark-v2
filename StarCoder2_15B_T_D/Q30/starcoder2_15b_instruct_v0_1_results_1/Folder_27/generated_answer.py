def insert_before_character(string):
    new_string = ''
    for i, c in enumerate(string):
        if c == 'N':
            new_string += 'j'
        new_string += c
    return new_string