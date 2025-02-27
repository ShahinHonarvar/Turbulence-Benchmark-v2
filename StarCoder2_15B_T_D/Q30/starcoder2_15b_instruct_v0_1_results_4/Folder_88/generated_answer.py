def insert_before_character(string):
    new_string = ''
    for i, c in enumerate(string):
        if c == 'a':
            new_string += 't'
        new_string += c
    return new_string