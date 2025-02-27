def insert_before_character(s):
    new_string = ''
    for i, c in enumerate(s):
        if c == '9':
            new_string += 'h'
        new_string += c
    return new_string