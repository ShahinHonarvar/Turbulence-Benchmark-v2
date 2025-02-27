def insert_after_character(input_string):
    result = ''
    for char in input_string:
        if char == 'j':
            result += 'jq'
        else:
            result += char
    return result