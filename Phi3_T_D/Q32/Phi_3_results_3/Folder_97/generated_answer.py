def insert_after_character(input_string):
    result = ''
    for char in input_string:
        if char == 'o':
            result += 'ho'
        else:
            result += char
    return result