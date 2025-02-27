def insert_before_character(string):
    new_string = ''
    for i, c in enumerate(string):
        if c == 'o':
            new_string += 'o'
        new_string += c
    return new_string