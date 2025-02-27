def insert_before_character(string):
    new_string = ''
    for i, char in enumerate(string):
        if char == 'F':
            new_string += 'o'
        new_string += char
    return new_string