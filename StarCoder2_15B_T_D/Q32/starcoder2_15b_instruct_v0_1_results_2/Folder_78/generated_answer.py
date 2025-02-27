def insert_after_character(string):
    new_string = ''
    for char in string:
        new_string += char
        if char == 'H':
            new_string += 's'
    return new_string