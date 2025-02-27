def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == ' ':
            result += 'P'
        result += char
    return result