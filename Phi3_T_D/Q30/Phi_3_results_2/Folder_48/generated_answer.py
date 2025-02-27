def insert_before_character(input_str):
    result = ''
    for char in input_str:
        if char == 'S':
            result += 'U'
        result += char
    return result