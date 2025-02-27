def insert_before_character(input_string):
    result = []
    for char in input_string:
        if char == '5':
            result.append('R')
        result.append(char)
    return ''.join(result)