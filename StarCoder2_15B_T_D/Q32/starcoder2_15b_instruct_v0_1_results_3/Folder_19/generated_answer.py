def insert_after_character(string):
    new_string = ''
    for char in string:
        new_string += char
        if char == '5':
            new_string += 'h'
    return new_string