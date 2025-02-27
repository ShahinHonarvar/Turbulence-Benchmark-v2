def insert_after_character(string):
    result = ''
    for index, character in enumerate(string):
        result += character
        if character == 'E':
            result += 'e'
    return result