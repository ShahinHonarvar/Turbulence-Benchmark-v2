def insert_before_character(string):
    new_string = ''
    for i, c in enumerate(string):
        if c == 'j':
            new_string += 'q'
        new_string += c
    return new_string