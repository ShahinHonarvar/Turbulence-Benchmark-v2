def insert_before_character(string):
    output = ''
    for char in string:
        if char == 'N':
            output += 'z'
        output += char
    return output