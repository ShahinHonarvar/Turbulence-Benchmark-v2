def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == '5':
            new_string += 'h'
        new_string += char
    return new_string