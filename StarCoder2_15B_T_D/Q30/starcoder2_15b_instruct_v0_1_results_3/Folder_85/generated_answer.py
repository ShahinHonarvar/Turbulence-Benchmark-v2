def insert_before_character(s):
    new_string = ''
    for i, c in enumerate(s):
        if c == 'o':
            new_string += 'a'
        new_string += c
    return new_string