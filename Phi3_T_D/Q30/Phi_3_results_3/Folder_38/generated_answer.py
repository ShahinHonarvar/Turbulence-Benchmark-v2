def insert_before_character(s):
    new_string = ''
    for char in s:
        if char == 'X':
            new_string += '6' + char
        else:
            new_string += char
    return new_string