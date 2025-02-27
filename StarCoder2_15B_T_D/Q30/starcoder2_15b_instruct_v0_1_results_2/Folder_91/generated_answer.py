def insert_before_character(string):
    output = ''
    for character in string:
        if character == 'a':
            output += '0a'
        else:
            output += character
    return output