def insert_after_character(string):
    new_string = ''
    for i, c in enumerate(string):
        new_string += c
        if c == 'm':
            new_string += 'N'
    return new_string