def insert_after_character(string):
    output = ''
    for char in string:
        output += char
        if char == 'Q':
            output += 'I'
    return output