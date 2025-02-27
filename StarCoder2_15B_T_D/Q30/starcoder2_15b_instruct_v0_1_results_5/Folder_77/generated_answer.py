def insert_before_character(string):
    new_string = ''
    for i, c in enumerate(string):
        if c == '9':
            new_string += 'h'
        new_string += c
    return new_string