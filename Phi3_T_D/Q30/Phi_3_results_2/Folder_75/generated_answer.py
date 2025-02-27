def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'U':
            result += 'qU'
        else:
            result += char
    return result