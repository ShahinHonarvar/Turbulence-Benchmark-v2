def insert_before_character(input_string):
    result = ''
    for character in input_string:
        if character == ' ':
            result += 'K' + character
        else:
            result += character
    return result