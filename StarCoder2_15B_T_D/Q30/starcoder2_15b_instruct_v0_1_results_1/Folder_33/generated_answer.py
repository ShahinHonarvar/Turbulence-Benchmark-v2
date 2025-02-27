def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 'a':
            new_string += 'n'
        new_string += char
    return new_string