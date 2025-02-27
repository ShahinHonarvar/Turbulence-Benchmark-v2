def insert_after_character(string):
    new_string = ''
    for i, char in enumerate(string):
        new_string += char
        if char == 'A':
            new_string += 'H'
    return new_string