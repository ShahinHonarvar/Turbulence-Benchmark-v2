def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 'm':
            new_string += 'N'
        new_string += char
    return new_string