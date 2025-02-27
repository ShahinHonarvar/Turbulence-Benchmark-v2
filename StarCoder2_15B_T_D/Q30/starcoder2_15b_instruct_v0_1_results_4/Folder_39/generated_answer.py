def insert_before_character(string):
    output = ''
    for char in string:
        if char == 'm':
            output += 'Qm'
        else:
            output += char
    return output