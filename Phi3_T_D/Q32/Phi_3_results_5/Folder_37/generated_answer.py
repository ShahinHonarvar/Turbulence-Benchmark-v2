def insert_after_character(input_string):
    result = ''
    for char in input_string:
        if char == 'U':
            result += 'Ua'
        else:
            result += char
    return result