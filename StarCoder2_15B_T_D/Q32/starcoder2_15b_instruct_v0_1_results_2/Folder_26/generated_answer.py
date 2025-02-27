def insert_after_character(string):
    new_string = ''
    for i, c in enumerate(string):
        new_string += c
        if c == 'r':
            new_string += 'w'
    return new_string