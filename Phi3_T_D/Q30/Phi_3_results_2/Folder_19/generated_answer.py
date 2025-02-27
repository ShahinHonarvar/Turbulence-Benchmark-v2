def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == '5':
            result += 'h' + char
        else:
            result += char
    return result