def insert_before_character(str):
    new_str = ''
    for i, c in enumerate(str):
        if c == 'S':
            new_str += 'US'
        else:
            new_str += c
    return new_str