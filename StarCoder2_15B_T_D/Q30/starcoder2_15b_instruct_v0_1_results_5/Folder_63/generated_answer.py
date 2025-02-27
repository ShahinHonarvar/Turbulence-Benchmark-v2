def insert_before_character(string):
    new_string = ''
    for char in string:
        new_string += char
        if char == '5':
            new_string += 'R'
    return new_string