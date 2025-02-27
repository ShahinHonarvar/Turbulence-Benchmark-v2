def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'u':
            result += 'U' + char
        else:
            result += char
    return result