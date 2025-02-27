def insert_after_character(input_string):
    result = ''
    for char in input_string:
        if char == 'r':
            result += 'wr'
        else:
            result += char
    return result