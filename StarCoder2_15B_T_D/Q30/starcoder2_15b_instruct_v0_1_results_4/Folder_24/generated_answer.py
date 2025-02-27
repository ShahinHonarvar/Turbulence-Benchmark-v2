def insert_before_character(string):
    output = ''
    for char in string:
        if char == '0':
            output += '40'
        else:
            output += char
    return output