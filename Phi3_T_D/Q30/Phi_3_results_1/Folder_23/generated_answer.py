def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'b':
            result += 'yb'
        else:
            result += char
    return result