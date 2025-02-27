def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 'a':
            new_string += 'W'
        new_string += char
    return new_string