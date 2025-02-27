def insert_after_character(string):
    new_string = ''
    for char in string:
        new_string += char
        if char == 'E':
            new_string += 'e'
    return new_string