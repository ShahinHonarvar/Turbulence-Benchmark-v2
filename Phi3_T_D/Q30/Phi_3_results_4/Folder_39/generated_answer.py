def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'm':
            result += 'Q' + char
        else:
            result += char
    return result