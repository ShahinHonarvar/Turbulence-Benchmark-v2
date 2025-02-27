def insert_before_character(input_str):
    result = ''
    for char in input_str:
        if char == 'a':
            result += 'a' + char
        else:
            result += char
    return result