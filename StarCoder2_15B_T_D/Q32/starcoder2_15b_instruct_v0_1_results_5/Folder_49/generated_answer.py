def insert_after_character(string):
    output = ''
    for char in string:
        output += char
        if char == 'i':
            output += 'i'
    return output