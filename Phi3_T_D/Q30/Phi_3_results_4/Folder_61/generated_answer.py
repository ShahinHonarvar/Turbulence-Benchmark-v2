def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'e':
            result += '0' + char
        else:
            result += char
    return result