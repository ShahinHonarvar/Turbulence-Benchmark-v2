def insert_after_character(text):
    output = ''
    for character in text:
        output += character
        if character == '5':
            output += 'R'
    return output