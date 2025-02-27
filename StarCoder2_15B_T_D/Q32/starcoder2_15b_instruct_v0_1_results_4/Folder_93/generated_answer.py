def insert_after_character(string):
    output = ''
    for character in string:
        if character == 'Y':
            output += '4'
        output += character
    return output