def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'U':
            result += 'TU'
        else:
            result += char
    return result