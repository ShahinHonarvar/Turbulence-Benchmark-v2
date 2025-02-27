def insert_after_character(s):
    modified_string = ''
    for char in s:
        modified_string += char
        if char == 'F':
            modified_string += 'm'
    return modified_string