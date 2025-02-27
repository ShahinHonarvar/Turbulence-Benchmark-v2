def insert_before_character(string):
    result = ''
    for character in string:
        if character == 'O':
            result += 'QO'
        else:
            result += character
    return result