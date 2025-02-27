def insert_before_character(string):
    output = ''
    for char in string:
        if char == 'a':
            output += 'A'
        output += char
    return output