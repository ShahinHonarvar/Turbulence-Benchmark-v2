def insert_before_character(string):
    output = ''
    for char in string:
        if char == ' ':
            output += 'X'
        output += char
    return output