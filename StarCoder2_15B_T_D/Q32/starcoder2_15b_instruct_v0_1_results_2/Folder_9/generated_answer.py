def insert_after_character(string):
    output_string = ''
    for character in string:
        if character == 'e':
            output_string += 'eE'
        else:
            output_string += character
    return output_string