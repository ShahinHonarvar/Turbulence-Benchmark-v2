def insert_after_character(string):
    result = ''
    for character in string:
        result += character
        if character == 'U':
            result += 'T'
    return result