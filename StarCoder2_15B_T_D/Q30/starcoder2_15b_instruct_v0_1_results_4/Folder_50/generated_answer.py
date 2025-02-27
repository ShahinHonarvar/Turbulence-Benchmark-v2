def insert_before_character(string):
    new_string = ''
    for i, c in enumerate(string):
        if c == 't':
            new_string += 'u'
        new_string += c
    return new_string