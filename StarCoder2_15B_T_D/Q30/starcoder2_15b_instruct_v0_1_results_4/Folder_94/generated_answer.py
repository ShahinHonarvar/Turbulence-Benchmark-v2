def insert_before_character(s):
    new_string = ''
    for i, c in enumerate(s):
        if c == ' ':
            new_string += '5'
        new_string += c
    return new_string