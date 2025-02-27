def insert_before_character(string):
    output = ''
    for char in string:
        if char == '0':
            output += '0'
        else:
            output += char
    return output