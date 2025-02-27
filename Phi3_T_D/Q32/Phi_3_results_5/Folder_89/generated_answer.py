def insert_after_character(s):
    new_string = ''
    for char in s:
        new_string += char
        if char == ' ':
            new_string += 'W'
    return new_string