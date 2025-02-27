def insert_after_character(input_str):
    result = ''
    for char in input_str:
        result += char
        if char == '9':
            result += 'h'
    return result