def insert_before_character(string):
    new_string = ''
    for i, char in enumerate(string):
        if char == '6':
            new_string += 'W6'
        else:
            new_string += char
    return new_string