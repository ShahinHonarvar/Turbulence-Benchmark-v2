def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'r':
            result += 'w' + char
        else:
            result += char
    return result