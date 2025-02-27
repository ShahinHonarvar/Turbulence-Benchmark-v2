def insert_before_character(input_str):
    result = ''
    for char in input_str:
        result += char + 'U' if char == 'U' else char
    return result