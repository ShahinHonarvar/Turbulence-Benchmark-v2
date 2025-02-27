def insert_after_character(value):
    result = ''
    for character in value:
        result += character
        if character == 's':
            result += 'w'
    return result