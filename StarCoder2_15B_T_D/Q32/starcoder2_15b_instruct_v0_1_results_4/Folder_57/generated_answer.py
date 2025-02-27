def insert_after_character(string):
    new_string = ''
    for i, char in enumerate(string):
        new_string += char
        if char == 's':
            new_string += 'w'
    return new_string