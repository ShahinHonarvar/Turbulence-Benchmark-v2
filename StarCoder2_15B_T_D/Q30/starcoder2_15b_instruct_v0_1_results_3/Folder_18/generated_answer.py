def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'K':
            result += 'lK'
        else:
            result += char
    return result