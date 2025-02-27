def insert_after_character(string):
    new_string = ''
    for i, char in enumerate(string):
        new_string += char
        if char == 'P':
            new_string += 'V'
    return new_string