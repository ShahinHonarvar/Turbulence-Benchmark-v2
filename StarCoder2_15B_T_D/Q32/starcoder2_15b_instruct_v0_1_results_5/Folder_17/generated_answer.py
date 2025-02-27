def insert_after_character(string):
    output = []
    for char in string:
        output.append(char)
        if char == 'Q':
            output.append('I')
    return ''.join(output)