def insert_before_character(s):
    modified_string = ''
    for char in s:
        modified_string += 'u' if char == 'u' else char
    return modified_string