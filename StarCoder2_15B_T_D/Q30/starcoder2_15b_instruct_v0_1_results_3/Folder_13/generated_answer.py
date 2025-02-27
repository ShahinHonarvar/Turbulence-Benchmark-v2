def insert_before_character(string):
    new_string = ''
    for i, c in enumerate(string):
        if c == 'x':
            new_string += 'N'
        new_string += c
    return new_string